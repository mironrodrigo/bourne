from cassandra.cluster import Cluster

def get_scylla_session():
    cluster = Cluster(["scylla-node"])
    return cluster.connect("bourne")