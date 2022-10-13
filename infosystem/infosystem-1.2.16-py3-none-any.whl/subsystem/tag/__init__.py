from infosystem.common import subsystem
from infosystem.subsystem.tag import resource, router, manager, controller


subsystem = subsystem.Subsystem(resource=resource.Tag,
                                router=router.Router,
                                manager=manager.Manager,
                                controller=controller.Controller)
