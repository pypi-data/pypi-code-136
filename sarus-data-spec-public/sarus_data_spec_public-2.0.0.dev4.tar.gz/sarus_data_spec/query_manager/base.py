from __future__ import annotations

from functools import reduce
from typing import Collection, Dict, List, Optional, cast

from sarus_data_spec.constants import PEP_TOKEN
from sarus_data_spec.manager.ops.asyncio.processor import routing
from sarus_data_spec.storage.typing import Storage
from sarus_data_spec.variant_constraint import (
    pep_constraint,
    public_constraint,
)
import sarus_data_spec.protobuf as sp
import sarus_data_spec.query_manager.simple_rules as compilation_rules
import sarus_data_spec.typing as st


class BaseQueryManager:
    def __init__(self, storage: Storage):
        self._storage = storage

    def storage(self) -> Storage:
        return self._storage

    def is_compliant(
        self,
        dataspec: st.DataSpec,
        kind: st.ConstraintKind,
        public_context: List[str],
        epsilon: Optional[float],
    ) -> bool:
        variant = self.variant(
            dataspec,
            kind,
            public_context,
            epsilon,
        )
        if variant:
            return variant.uuid() == dataspec.uuid()
        else:
            return False

    def variant(
        self,
        dataspec: st.DataSpec,
        kind: st.ConstraintKind,
        public_context: List[str],
        epsilon: Optional[float],
    ) -> Optional[st.DataSpec]:
        return compilation_rules.compile(
            self, dataspec, kind, public_context, epsilon
        )

    def variants(self, dataspec: st.DataSpec) -> Collection[st.DataSpec]:
        attributes = self.storage().referring(
            dataspec, type_name=sp.type_name(sp.Attribute)
        )
        all_attributes: Dict[str, str] = reduce(
            lambda x, y: {**x, **y},
            map(lambda x: x.properties(), attributes),
            dict(),
        )
        variants_uuids = [
            uuid
            for key, uuid in all_attributes.items()
            if key in sp.ConstraintKind.DESCRIPTOR.values_by_name
        ]
        variants = [
            cast(st.DataSpec, self.storage().referrable(uuid))
            for uuid in variants_uuids
        ]
        return [var for var in variants if var]

    def variant_constraint(
        self, dataspec: st.DataSpec
    ) -> Optional[st.VariantConstraint]:
        constraints = self.storage().referring(
            dataspec, type_name=sp.type_name(sp.VariantConstraint)
        )
        if len(constraints) == 0:
            return None
        elif len(constraints) == 1:
            return cast(st.VariantConstraint, list(constraints)[0])
        else:
            raise ValueError(
                f"More than one variant_constraint attached to {dataspec}"
            )

    def verified_constraints(
        self, dataspec: st.DataSpec
    ) -> List[st.VariantConstraint]:
        """Return the list of VariantConstraints attached to a DataSpec.

        A VariantConstraint attached to a DataSpec means that the DataSpec
        verifies the constraint.
        """
        constraints = self.storage().referring(
            dataspec, type_name=sp.type_name(sp.VariantConstraint)
        )
        return cast(List[st.VariantConstraint], list(constraints))

    def verifies(
        self,
        variant_constraint: st.VariantConstraint,
        kind: st.ConstraintKind,
        public_context: Collection[str],
        epsilon: Optional[float],
    ) -> bool:
        """Check if the constraint attached to a Dataspec meets requirements.

        This function is useful because comparisons are not straightforwards.
        For instance, a Dataspec might have the variant constraint SYNTHETIC
        attached to it. This synthetic dataspec also verifies the DP constraint
        and the PUBLIC constraint.

        Args:
            variant_constraint: VariantConstraint attached to the Dataspec
            kind: constraint kind to verify compliance with
            public_context: actual current public context
            epsilon: current privacy consumed
        """
        return compilation_rules.verifies(
            query_manager=self,
            variant_constraint=variant_constraint,
            kind=kind,
            public_context=public_context,
            epsilon=epsilon,
        )

    def is_public(self, dataspec: st.DataSpec) -> bool:
        """Return True if the dataspec is public.

        Some DataSpecs are intrinsically Public, this is the case if they are
        freely available externally, they can be tagged so and will never be
        considered otherwise.

        This function returns True in the following cases:
        - The dataspec is an ML model
        - The dataspec is transformed but all its inputs are public

        This functions creates a VariantConstraint on the DataSpec to cache the
        PUBLIC constraint.
        """
        # TODO fetch real context and epsilon
        public_context: List[str] = []
        epsilon = 0.0
        kind = st.ConstraintKind.PUBLIC

        # Does any saved constraint yet verifies that the Dataspec is public
        for constraint in self.verified_constraints(dataspec):
            if self.verifies(constraint, kind, public_context, epsilon):
                return True

        # Determine is the Dataspec is public
        if dataspec.is_transformed():
            # Returns true if the DataSpec derives only from public
            args_parents, kwargs_parents = dataspec.parents()
            is_public = all(
                [self.is_public(ds) for ds in args_parents]
                + [self.is_public(ds) for ds in kwargs_parents.values()]
            )
        elif dataspec.prototype() == sp.Scalar:
            scalar = cast(st.Scalar, dataspec)
            if scalar.is_model():
                is_public = True
        else:
            is_public = False

        # save variant constraint
        if is_public:
            public_constraint(dataspec)

        return is_public

    def pep_token(self, dataspec: st.DataSpec) -> Optional[str]:
        """Return a token if the dataspec is PEP, otherwise return None.

        DataSpec.pep_token() returns a PEP token if the dataset is PEP and None
        otherwise. The PEP token is stored in the properties of the
        VariantConstraint. It is a hash initialized with a value when the
        Dataset is protected.

        If a transform does not preserve the PEID then the token is set to None
        If a transform preserves the PEID assignment but changes the rows (e.g.
        sample, shuffle, filter,...) then the token's value is changed If a
        transform does not change the rows (e.g. selecting a column, adding a
        scalar,...) then the token is passed without change

        A Dataspec is PEP if its PEP token is not None. Two PEP Dataspecs are
        aligned (i.e. they have the same number of rows and all their rows have
        the same PEID) if their tokens are equal.
        """
        if dataspec.prototype() == sp.Scalar:
            return None

        dataset = cast(st.Dataset, dataspec)

        # TODO fetch real context and epsilon
        public_context: List[str] = []
        epsilon = 0.0
        kind = st.ConstraintKind.PEP

        # Does any constraint yet verifies that the Dataset is PEP
        for constraint in self.verified_constraints(dataset):
            if self.verifies(constraint, kind, public_context, epsilon):
                return constraint.properties()[PEP_TOKEN]

        # Compute the PEP token
        if not dataset.is_transformed():
            return None

        transform = dataset.transform()
        OpClass = routing.get_dataset_op(transform)
        pep_token = OpClass(dataset).pep_token(public_context, epsilon)
        if pep_token is not None:
            pep_constraint(
                dataspec=dataset,
                token=pep_token,
                required_context=[],
                epsilon=0.0,
            )

        return pep_token

    def is_pe_preserving(self, transform: st.Transform) -> bool:
        raise NotImplementedError("is_pe_preserving")

    def is_differentially_private(self, transform: st.Transform) -> bool:
        raise NotImplementedError("is_differentially_private")

    def transform_equivalent(
        self, transform: st.Transform, dp: bool
    ) -> Optional[st.Transform]:
        """Return the DP or non-DP version of a transform.

        Return None if the requested DP equivalent does not exist.
        """
        raise NotImplementedError("transform_equivalent")
