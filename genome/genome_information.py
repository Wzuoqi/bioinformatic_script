from sys import argv
import re

sequencelist=[x.strip() for x in open(argv[1]).readlines()]
seq_dict = {}
for x in sequencelist :
	if x.startswith('>') :
		dict_id = x[1:]
		seq_dict[dict_id] = []
	else :
		seq_dict[dict_id].append(x)

len_sum=0
gaps_sum=0
gaps_number=0
GC_num=0
len_list=[]
for x in seq_dict:
	tmp=(''.join(seq_dict[x])).strip()
	len_list.append(len(tmp))
	len_sum+=len(tmp)
	gaps_len=tmp.count('N')
	gaps_sum+=gaps_len
	m=re.findall(r'N+',tmp)
	tmp_num=len(m)
	gaps_number+=tmp_num
	tmp_GC=tmp.count('G')+tmp.count('C')
	GC_num+=tmp_GC
Sequence_Number = str(len(seq_dict.keys()))
Genome_Size = str((len_sum/1000)/1000)
Gaps_length = str((gaps_sum/1000)/1000)
GC_content = str((GC_num/len_sum)*100)

# print('Sequence Number: '+str(len(seq_dict.keys())))
# print('Genome Size: '+str((len_sum/1000)/1000)+' Mb')
# print('Gaps length: '+str((gaps_sum/1000)/1000)+' Mb')
# print('Gaps number: '+str(gaps_number))
# print('G+C content: '+str((GC_num/len_sum)*100)+' %')
len_list.sort(reverse=True)
half_len=len_sum/2
sum_len=0
for x in len_list:
	sum_len+=x
	if sum_len > half_len:
		# print('N50: '+str(x/1000)+' Kb')
		N50 = str(x/1000)
		break
	else:
		pass

print(argv[1][:-4]+'\t'+Sequence_Number+'\t'+Genome_Size+'\t'+Gaps_length+'\t'+GC_content+'\t'+N50)