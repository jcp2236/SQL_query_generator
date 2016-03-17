import os

recon = 'P:\\Technical Services and Research\\Active Research\\JPullin\\Reconciliations'

fpath = os.path.join(recon, 'query_invoice.txt')
qpath = os.path.join(recon, 'query_new.txt')

list_of_lists = []
query_list = []

with open(fpath) as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(' ')]
        new_list = [''.join("'" + item + "'") for item in inner_list]
        list_of_lists.append(new_list)


for CT in list_of_lists:
    query = 'CT_Tag_ID = ' + '\n'.join(CT) + ' OR '
    query_list.append(query)

with open(qpath, 'w') as q:
    for line in query_list:
        q.write(line)
    print "Done"


print query_list
