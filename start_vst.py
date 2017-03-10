#!/Applications/anaconda/bin/python
import webbrowser
# webrowser section
new = 2
url = "https://vst.gsfc.nasa.gov/vst/index.php?title=Special:UserLogin"
download = "https://vst.gsfc.nasa.gov/vst/img_auth.php/1/1d/Code600_combolist.plink.xls"
print ("Opening VST login page and file download. Login and refresh second tab to download file.")
webbrowser.open(url,new=new)
webbrowser.open(download,new=new)
