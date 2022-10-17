"""Static Query for the server"""

GET_NODE = """
query GetNode($network: String!, $node_id: String!){
  getNode(network: $network, node_id: $node_id) {
    version
    node_id
    alias
    color
    network
    address {
      type
      host
      port
    } 
    os_info {
      os
      version
      architecture
    }
    node_info {
      implementation
      version
    }
    timezone
    last_update
  }
}
"""

GET_NODES = """
query GetNodes($network: String!){
  getNodes(network: $network) {
    version
    node_id
    alias
    color
    network
    address {
      type
      host
      port
    } 
    os_info {
      os
      version
      architecture
    }
    node_info {
      implementation
      version
    }
    timezone
    last_update
  }
}
"""

GET_METRIC_ONE = """
query MetricOne($node_id: String!, $first: Int!, $last: Int!){
  metricOne(node_id: $node_id, first: $first, last: $last) {
    page_info {
      start
      end
      has_next
    }
    channels_info {
      node_id
      channel_id
      node_alias
      color
      capacity
      forwards {
        direction
        status
        failure_reason
        failure_code
        timestamp
      }
      up_time {
        event
        status
        timestamp
      }
      online
      last_update
      direction
      fee {
        base
        per_msat
      }
      limits {
        min
        max
      }
    }
    up_time {
      event
      channels {
        tot_channels
        summary {
          node_id
          alias
          color
          channel_id
          state
        }
      }
      forwards {
        completed
        failed
      }
      timestamp
      fee {
        base
        per_msat
      }
      limits {
        min
        max
      }
    }
  }
}
"""
