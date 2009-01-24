"Converts part of BBCode to wiki formatting, using regular expressions."


import re
import sys




def sub_b(in_str):
	return re.sub(r'\[/?b\]', "'''", in_str)

def sub_i(in_str):
	return re.sub(r'\[/?i\]', "''", in_str)


# numberd lists
def sub_nlist(in_str):
	handle_nlist = lambda m: m.group(0)[8:-7].replace('[*]', '\n#') + '\n\n'
	return re.sub(r'\[list=1\].*\[/list\]', handle_nlist, in_str)

# Converting URL's.

def sub_turl(in_str):
	'[url=LINK]TITLE[/url] -> [LINK TITLE]'
	def parse_url(m):
		l=re.split(r'\[url=([^\]]*)]([^\[]*)\[/url\]', m.group(0))
		return '['+ l[1] + ' ' + l[2] + ']'
	in_str = re.sub(r'\[url=([^\]])*]([^\[])*\[/url\]', parse_url, in_str)
	return in_str

def sub_url(in_str):
	'[url]LINK[/url] -> [LINK]'
	return re.sub(r'\[url\]([^\[])*\[/url\]', lambda m: '['+m.group(0)[5:-6]+']', in_str)


def sub_size(s):
	def parse_size(m):
		l = re.split(r'\[size=(\d*)\]([^\[]*)\[/size\]', m.group(0))
		return '<span style="font-size:%spx">%s</span>' % (l[1], l[2])
	return re.sub(r'\[size=\d*\]([^\[])*\[/size\]', parse_size, s)


def convert(in_str):
	in_str = sub_b(in_str)
	in_str = sub_i(in_str)

	# \number doesn't work :(
	in_str = re.sub(r'\[u\]', '<u>', in_str)
	in_str = re.sub(r'\[/u\]', '</u>', in_str)
	
	in_str = in_str.replace('\n', '<br>')

	in_str = sub_nlist(in_str)

	in_str = sub_url(in_str)
	in_str = sub_turl(in_str)

	in_str = in_str.replace('[center]', '<center>')
	in_str = in_str.replace('[/center]', '</center>')

	in_str = sub_size(in_str)
	

	return in_str


if __name__ == "__main__":
	in_page = sys.stdin.read()

	print convert(in_page)



