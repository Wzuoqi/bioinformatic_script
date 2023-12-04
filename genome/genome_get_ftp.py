# usage
# 在当前目录下的GA_name.id中输入需要下载的GCA号
# 输出需要的ftp地址
import requests
import re
def get_ftp_directory(url_name):
    response = requests.get(url_name)
    response.encoding = "utf-8"
    # print(response.text)
    directory = re.findall(
        r'<a href="(.*)">FTP directory for GenBank assembly</a>', response.text, flags=0)
    if directory != []:
        return directory[0]

# print(get_ftp_directory("https://www.ncbi.nlm.nih.gov/assembly/GCA_028551675.1"))
Assembly_List = open("./GA_name.id", encoding='utf-8')
for GA_id in Assembly_List:
    Assembly_Website = "https://www.ncbi.nlm.nih.gov/assembly/" + GA_id.rstrip()
    GA_directory = get_ftp_directory(Assembly_Website)
    if GA_directory:
        project_name = re.findall(r'/(GCA_.*?)$',GA_directory,flags=0)
        fna_name = GA_directory+'/'+project_name[0]+'_genomic.fna.gz'
        gff_name = GA_directory+'/'+project_name[0]+'_genomic.gff.gz'
        print(fna_name)
        # print(gff_name)



