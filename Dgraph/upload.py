from neo4j import GraphDatabase

# 建立一个Neo4j会话
driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'NEO123456neo'))

