# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testFlame
   Description :
   Author :       liaozhaoyan
   date：          2022/10/5
-------------------------------------------------
   Change Activity:
                   2022/10/5:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

from graphSvg import CgraphTree
from quickSvg import Flame

orig = """1)               |  __do_fault() {
1)               |    special_mapping_fault() {
1)   0.516 us    |      vdso_fault();
1)   1.032 us    |    }
1)               |    _cond_resched() {
1)   0.165 us    |      rcu_all_qs();
1)   0.477 us    |    }
1)   2.658 us    |  }"""

orig2 = """1)               |  __do_fault() {
1)   ==========> |
1)               |    smp_irq_work_interrupt() {
1)               |      irq_enter() {
1)               |        rcu_irq_enter() {
1)   0.179 us    |          rcu_nmi_enter();
1)   0.529 us    |        }
1)   0.924 us    |      }
1)               |      __wake_up() {
1)               |        __wake_up_common_lock() {
1)   0.173 us    |          _raw_spin_lock_irqsave();
1)   0.208 us    |          __wake_up_common();
1)   0.398 us    |          _raw_spin_unlock_irqrestore();
1)   1.681 us    |        }
1)   2.011 us    |      }
1)               |      irq_exit() {
1)   0.348 us    |        idle_cpu();
1)               |        rcu_irq_exit() {
1)   0.492 us    |          rcu_nmi_exit();
1)   0.898 us    |        }
1)   2.250 us    |      } /* irq_exit */
1)   6.689 us    |    }
1)   <========== |
1)               |    pte_alloc_one() {
1)               |      alloc_pages_current() {
1)   0.162 us    |        get_task_policy.part.31();
1)   0.490 us    |        policy_nodemask();
1)   0.298 us    |        policy_node();
1)               |        __alloc_pages_nodemask() {
1)               |          _cond_resched() {
1)   0.154 us    |            rcu_all_qs();
1)   0.455 us    |          }
1)   0.157 us    |          __next_zones_zonelist();
1)               |          get_page_from_freelist() {
1)   0.418 us    |            __inc_numa_state();
1)   0.154 us    |            __inc_numa_state();
1)   2.248 us    |          }
1)   3.792 us    |        }
1)   5.796 us    |      }
1)   0.574 us    |      inc_zone_page_state();
1)   7.128 us    |    }
1)               |    ext4_filemap_fault [ext4]() {
1)               |      down_read() {
1)               |        _cond_resched() {
1)   0.153 us    |          rcu_all_qs();
1)   0.456 us    |        }
1)   0.772 us    |      }
1)               |      filemap_fault() {
1)               |        pagecache_get_page() {
1)   0.540 us    |          find_get_entry();
1)   1.305 us    |        }
1)               |        _cond_resched() {
1)   0.153 us    |          rcu_all_qs();
1)   0.457 us    |        }
1)   2.383 us    |      }
1)   0.152 us    |      up_read();
1)   3.971 us    |    }
1) + 20.084 us   |  }"""


def getValue(data):
    return data['us']


def getNote(tree, node):
    root = tree.get_node(tree.root)
    perRoot = node.data['us'] / root.data['us'] * 100.0

    parent = tree.parent(node.identifier)
    if parent is None:
        perParent = 100.0
    else:
        perParent = node.data['us'] / parent.data['us'] * 100.0
    return "cost %f us, %f%% from root, %f%% from parent" % (node.data['us'], perRoot, perParent)


def test(lines):
    graph = CgraphTree()
    tree = graph.tree(lines)
    graph.walk(tree)
    f = Flame("flame.svg")
    f.render(tree, getValue, getNote, "call flame")


if __name__ == "__main__":
    test(orig2.split('\n'))
    pass
