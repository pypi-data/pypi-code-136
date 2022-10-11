# Copyright 2020 Creu Blanca
# Copyright 2021 Tecnativa - Víctor Martínez
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from logging import getLogger

from odoo import SUPERUSER_ID, api, fields, models
from odoo.osv.expression import FALSE_DOMAIN, NEGATIVE_TERM_OPERATORS, OR, TRUE_DOMAIN

_logger = getLogger(__name__)


class DmsSecurityMixin(models.AbstractModel):
    _name = "dms.security.mixin"
    _description = "DMS Security Mixin"

    # Submodels must define this field that points to the owner dms.directory
    _directory_field = "directory_id"

    res_model = fields.Char(string="Linked attachments model", index=True)
    res_id = fields.Integer(string="Linked attachments record ID", index=True)
    record_ref = fields.Reference(
        string="Record Referenced", compute="_compute_record_ref", selection=[]
    )
    permission_read = fields.Boolean(
        compute="_compute_permissions",
        search="_search_permission_read",
        string="Read Access",
    )
    permission_create = fields.Boolean(
        compute="_compute_permissions",
        search="_search_permission_create",
        string="Create Access",
    )
    permission_write = fields.Boolean(
        compute="_compute_permissions",
        search="_search_permission_write",
        string="Write Access",
    )
    permission_unlink = fields.Boolean(
        compute="_compute_permissions",
        search="_search_permission_unlink",
        string="Delete Access",
    )

    @api.depends("res_model", "res_id")
    def _compute_record_ref(self):
        for record in self:
            if record.res_model and record.res_id:
                record.record_ref = "{},{}".format(record.res_model, record.res_id)

    def _compute_permissions(self):
        """Get permissions for the current record.

        ⚠ Not very performant; only display field on form views.
        """
        # Superuser unrestricted 🦸
        if self.env.uid == SUPERUSER_ID:
            self.update(
                {
                    "permission_create": True,
                    "permission_read": True,
                    "permission_unlink": True,
                    "permission_write": True,
                }
            )
            return
        # Update according to presence when applying ir.rule
        creatable = self._filter_access_rules("create")
        readable = self._filter_access_rules("read")
        unlinkable = self._filter_access_rules("unlink")
        writeable = self._filter_access_rules("write")
        for one in self:
            one.update(
                {
                    "permission_create": bool(one & creatable),
                    "permission_read": bool(one & readable),
                    "permission_unlink": bool(one & unlinkable),
                    "permission_write": bool(one & writeable),
                }
            )

    @api.model
    def _get_domain_by_inheritance(self, operation):
        """Get domain for inherited accessible records."""
        if self.env.uid == SUPERUSER_ID:
            return []
        inherited_access_field = "storage_id_inherit_access_from_parent_record"
        if self._name != "dms.directory":
            inherited_access_field = "{}.{}".format(
                self._directory_field, inherited_access_field,
            )
        inherited_access_domain = [(inherited_access_field, "=", True)]
        domains = []
        # Get all used related records
        related_groups = self.sudo().read_group(
            inherited_access_domain + [("res_model", "!=", False)],
            ["res_id:array_agg"],
            ["res_model"],
        )
        for group in related_groups:
            try:
                model = self.env[group["res_model"]]
            except KeyError:
                # Model not registered. This is normal if you are upgrading the
                # database. Otherwise, you probably have garbage DMS data.
                # These records will be accessible by DB users only.
                domains.append(
                    [
                        ("res_model", "=", group["res_model"]),
                        (True, "=", self.env.user.has_group("base.group_user")),
                    ]
                )
                continue
            # Check model access only once per batch
            if not model.check_access_rights(operation, raise_exception=False):
                continue
            domains.append([("res_model", "=", model._name), ("res_id", "=", False)])
            # Check record access in batch too
            related_ok = model.browse(group["res_id"])._filter_access_rules(operation)
            if not related_ok:
                continue
            domains.append(
                [("res_model", "=", model._name), ("res_id", "in", related_ok.ids)]
            )
        result = inherited_access_domain + OR(domains)
        return result

    @api.model
    def _get_access_groups_query(self, operation):
        """Return the query to select access groups."""
        operation_check = {
            "create": "AND dag.perm_inclusive_create",
            "read": "",
            "unlink": "AND dag.perm_inclusive_unlink",
            "write": "AND dag.perm_inclusive_write",
        }[operation]
        select = """
            SELECT
                dir_group_rel.aid
            FROM
                dms_directory_complete_groups_rel AS dir_group_rel
                INNER JOIN dms_access_group AS dag
                    ON dir_group_rel.gid = dag.id
                INNER JOIN dms_access_group_users_rel AS users
                    ON users.gid = dag.id
            WHERE
                users.uid = %s {}
            """.format(
            operation_check
        )
        return (select, (self.env.uid,))

    @api.model
    def _get_domain_by_access_groups(self, operation):
        """Get domain for records accessible applying DMS access groups."""
        result = [
            (
                "%s.storage_id_inherit_access_from_parent_record"
                % self._directory_field,
                "=",
                False,
            ),
            (
                self._directory_field,
                "inselect",
                self._get_access_groups_query(operation),
            ),
        ]
        return result

    @api.model
    def _get_permission_domain(self, operator, value, operation):
        """Abstract logic for searching computed permission fields."""
        _self = self
        # HACK While computing ir.rule domain, you're always superuser, so if
        # you're superuser but `value` is an `int`, we can assume safely that
        # you're checking permissions for another user (see the corresponding
        # rules in `security.xml`)
        # TODO Remove hack in v13, where sudo() and with_user() differ?
        if self.env.uid == SUPERUSER_ID and isinstance(value, int):
            _self = self.sudo(value)
            value = bool(value)
        # Tricky one, to know if you want to search
        # positive or negative access
        positive = (operator not in NEGATIVE_TERM_OPERATORS) == bool(value)
        if _self.env.uid == SUPERUSER_ID:
            return TRUE_DOMAIN if positive else FALSE_DOMAIN
        # Obtain and combine domains
        result = OR(
            [
                _self._get_domain_by_access_groups(operation),
                _self._get_domain_by_inheritance(operation),
            ]
        )
        if not positive:
            result.insert(0, "!")
        return result

    @api.model
    def _search_permission_create(self, operator, value):
        return self._get_permission_domain(operator, value, "create")

    @api.model
    def _search_permission_read(self, operator, value):
        return self._get_permission_domain(operator, value, "read")

    @api.model
    def _search_permission_unlink(self, operator, value):
        return self._get_permission_domain(operator, value, "unlink")

    @api.model
    def _search_permission_write(self, operator, value):
        return self._get_permission_domain(operator, value, "write")
