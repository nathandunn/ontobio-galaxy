
import argparse
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


from ontobio.ontol_factory import OntologyFactory
from ontobio.assoc_factory import AssociationSetFactory



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample script to open phenotypes')
    args = parser.parse_args()
    parser.add_argument('input', help='Input')

    ## Create an ontology factory in order to fetch HPO
    ofactory = OntologyFactory()
    ont = ofactory.create("hp")

    ## Create an association factory to get gene-phenotype associations
    afactory = AssociationSetFactory()
    ## Load Associations from Monarch. Note the first time this runs Jupyter will show '*' - be patient
    aset = afactory.create(ontology=ont, subject_category='gene', object_category='phenotype', taxon='NCBITaxon:9606')

    ## Run enrichment tests using all classes in ontology
    enr = aset.enrichment_test(subjects=gene_ids, threshold=0.00005, labels=True)


    for r in enr[:20]:
            print("{:8.3g} {} {:40s}".format(r['p'],r['c'],str(r['n'])))

