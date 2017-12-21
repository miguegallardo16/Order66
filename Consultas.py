import rdflib

g = rdflib.Graph()

g.parse("chromosome.rdf")

qres1 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a rdfs:label ?aDescription .
       }""")

qres2 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a dcterms:identifier ?aDescription .
       }""")

qres3 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a foaf:primaryTopicOf ?aDescription .
       }""")

qres4 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a rdf:type ?aDescription .
       }""")

qres5 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a rdfs:seeAlso ?aDescription .
       }""")

qres6 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a skos:exactMatch ?aDescription .
       }""")

qres7 = g.query(
    """SELECT DISTINCT ?aDescription
       WHERE {
          ?a rdfs:comment ?aDescription .
       }""")

for row in qres1:
    print(row)

for row in qres2:
    print(row)

for row in qres3:
    print(row)

for row in qres4:
    print(row)

for row in qres5:
    print(row)

for row in qres6:
    print(row)

for row in qres7:
    print(row)



