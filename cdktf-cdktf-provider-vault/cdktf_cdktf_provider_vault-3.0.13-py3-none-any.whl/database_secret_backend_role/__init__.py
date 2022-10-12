'''
# `vault_database_secret_backend_role`

Refer to the Terraform Registory for docs: [`vault_database_secret_backend_role`](https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class DatabaseSecretBackendRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.databaseSecretBackendRole.DatabaseSecretBackendRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role vault_database_secret_backend_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        creation_statements: typing.Sequence[builtins.str],
        db_name: builtins.str,
        name: builtins.str,
        default_ttl: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        renew_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        revocation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        rollback_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role vault_database_secret_backend_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: The path of the Database Secret Backend the role belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#backend DatabaseSecretBackendRole#backend}
        :param creation_statements: Database statements to execute to create and configure a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#creation_statements DatabaseSecretBackendRole#creation_statements}
        :param db_name: Database connection to use for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#db_name DatabaseSecretBackendRole#db_name}
        :param name: Unique name for the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#name DatabaseSecretBackendRole#name}
        :param default_ttl: Default TTL for leases associated with this role, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#default_ttl DatabaseSecretBackendRole#default_ttl}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#id DatabaseSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_ttl: Maximum TTL for leases associated with this role, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#max_ttl DatabaseSecretBackendRole#max_ttl}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#namespace DatabaseSecretBackendRole#namespace}
        :param renew_statements: Database statements to execute to renew a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#renew_statements DatabaseSecretBackendRole#renew_statements}
        :param revocation_statements: Database statements to execute to revoke a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#revocation_statements DatabaseSecretBackendRole#revocation_statements}
        :param rollback_statements: Database statements to execute to rollback a create operation in the event of an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#rollback_statements DatabaseSecretBackendRole#rollback_statements}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabaseSecretBackendRoleConfig(
            backend=backend,
            creation_statements=creation_statements,
            db_name=db_name,
            name=name,
            default_ttl=default_ttl,
            id=id,
            max_ttl=max_ttl,
            namespace=namespace,
            renew_statements=renew_statements,
            revocation_statements=revocation_statements,
            rollback_statements=rollback_statements,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetRenewStatements")
    def reset_renew_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRenewStatements", []))

    @jsii.member(jsii_name="resetRevocationStatements")
    def reset_revocation_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevocationStatements", []))

    @jsii.member(jsii_name="resetRollbackStatements")
    def reset_rollback_statements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollbackStatements", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="creationStatementsInput")
    def creation_statements_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "creationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="dbNameInput")
    def db_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="renewStatementsInput")
    def renew_statements_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "renewStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="revocationStatementsInput")
    def revocation_statements_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "revocationStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="rollbackStatementsInput")
    def rollback_statements_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rollbackStatementsInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="creationStatements")
    def creation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStatements"))

    @creation_statements.setter
    def creation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "creation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "db_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "default_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="renewStatements")
    def renew_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "renewStatements"))

    @renew_statements.setter
    def renew_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "renew_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renewStatements", value)

    @builtins.property
    @jsii.member(jsii_name="revocationStatements")
    def revocation_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "revocationStatements"))

    @revocation_statements.setter
    def revocation_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "revocation_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revocationStatements", value)

    @builtins.property
    @jsii.member(jsii_name="rollbackStatements")
    def rollback_statements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rollbackStatements"))

    @rollback_statements.setter
    def rollback_statements(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatabaseSecretBackendRole, "rollback_statements").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollbackStatements", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.databaseSecretBackendRole.DatabaseSecretBackendRoleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend": "backend",
        "creation_statements": "creationStatements",
        "db_name": "dbName",
        "name": "name",
        "default_ttl": "defaultTtl",
        "id": "id",
        "max_ttl": "maxTtl",
        "namespace": "namespace",
        "renew_statements": "renewStatements",
        "revocation_statements": "revocationStatements",
        "rollback_statements": "rollbackStatements",
    },
)
class DatabaseSecretBackendRoleConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        backend: builtins.str,
        creation_statements: typing.Sequence[builtins.str],
        db_name: builtins.str,
        name: builtins.str,
        default_ttl: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        renew_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        revocation_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        rollback_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: The path of the Database Secret Backend the role belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#backend DatabaseSecretBackendRole#backend}
        :param creation_statements: Database statements to execute to create and configure a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#creation_statements DatabaseSecretBackendRole#creation_statements}
        :param db_name: Database connection to use for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#db_name DatabaseSecretBackendRole#db_name}
        :param name: Unique name for the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#name DatabaseSecretBackendRole#name}
        :param default_ttl: Default TTL for leases associated with this role, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#default_ttl DatabaseSecretBackendRole#default_ttl}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#id DatabaseSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_ttl: Maximum TTL for leases associated with this role, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#max_ttl DatabaseSecretBackendRole#max_ttl}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#namespace DatabaseSecretBackendRole#namespace}
        :param renew_statements: Database statements to execute to renew a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#renew_statements DatabaseSecretBackendRole#renew_statements}
        :param revocation_statements: Database statements to execute to revoke a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#revocation_statements DatabaseSecretBackendRole#revocation_statements}
        :param rollback_statements: Database statements to execute to rollback a create operation in the event of an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#rollback_statements DatabaseSecretBackendRole#rollback_statements}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DatabaseSecretBackendRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument creation_statements", value=creation_statements, expected_type=type_hints["creation_statements"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument renew_statements", value=renew_statements, expected_type=type_hints["renew_statements"])
            check_type(argname="argument revocation_statements", value=revocation_statements, expected_type=type_hints["revocation_statements"])
            check_type(argname="argument rollback_statements", value=rollback_statements, expected_type=type_hints["rollback_statements"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
            "creation_statements": creation_statements,
            "db_name": db_name,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if id is not None:
            self._values["id"] = id
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if namespace is not None:
            self._values["namespace"] = namespace
        if renew_statements is not None:
            self._values["renew_statements"] = renew_statements
        if revocation_statements is not None:
            self._values["revocation_statements"] = revocation_statements
        if rollback_statements is not None:
            self._values["rollback_statements"] = rollback_statements

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def backend(self) -> builtins.str:
        '''The path of the Database Secret Backend the role belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#backend DatabaseSecretBackendRole#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def creation_statements(self) -> typing.List[builtins.str]:
        '''Database statements to execute to create and configure a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#creation_statements DatabaseSecretBackendRole#creation_statements}
        '''
        result = self._values.get("creation_statements")
        assert result is not None, "Required property 'creation_statements' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def db_name(self) -> builtins.str:
        '''Database connection to use for this role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#db_name DatabaseSecretBackendRole#db_name}
        '''
        result = self._values.get("db_name")
        assert result is not None, "Required property 'db_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique name for the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#name DatabaseSecretBackendRole#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Default TTL for leases associated with this role, in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#default_ttl DatabaseSecretBackendRole#default_ttl}
        '''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#id DatabaseSecretBackendRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Maximum TTL for leases associated with this role, in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#max_ttl DatabaseSecretBackendRole#max_ttl}
        '''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#namespace DatabaseSecretBackendRole#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def renew_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Database statements to execute to renew a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#renew_statements DatabaseSecretBackendRole#renew_statements}
        '''
        result = self._values.get("renew_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def revocation_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Database statements to execute to revoke a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#revocation_statements DatabaseSecretBackendRole#revocation_statements}
        '''
        result = self._values.get("revocation_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rollback_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Database statements to execute to rollback a create operation in the event of an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/database_secret_backend_role#rollback_statements DatabaseSecretBackendRole#rollback_statements}
        '''
        result = self._values.get("rollback_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretBackendRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatabaseSecretBackendRole",
    "DatabaseSecretBackendRoleConfig",
]

publication.publish()
