#!/usr/bin/env python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import sys
import os


def plot_sv(in_dir, chr_lens, out_pic):
	print("Reading datas")
	data_db = {}
	type_list = []
	f_cnt = 0
	f_list = []
	for fn in os.listdir(in_dir):
		if fn.split('.')[-1].lower() == 'bed':
			f_cnt += 1
			f_list.append(fn.split('.')[0])
			print("\tReading "+fn)
			ft = fn.split('.')[0]
			with open(os.path.join(in_dir, fn), 'r') as fin:
				for line in fin:
					if line[0] == '#':
						continue
					data = line.strip().split()
					chrn = data[0]
					if chrn.startswith('contig') or chrn.startswith('tig'):
						continue
					sp = int(data[1])
					ep = int(data[2])
					type = data[6]
					if chrn not in data_db:
						data_db[chrn] = {}
					if type not in data_db[chrn]:
						data_db[chrn][type] = {}
					if type not in type_list:
						type_list.append(type)
					if ft not in data_db[chrn][type]:
						data_db[chrn][type][ft] = []
					data_db[chrn][type][ft].append([sp, ep])

	print("Loading chr length")
	chr_len = {}
	chr_list = []
	with open(chr_lens, 'r') as fin:
		for line in fin:
			data = line.strip().split()
			chr_list.append(data[0])
			chr_len[data[0]] = int(data[1])

	chr_cnt = len(data_db)
	y_cnt = chr_cnt*f_cnt
	print("Ploting SVs")
	h = (1-(len(type_list)-1)*.2)/len(type_list)
	type_offset = {}
	sh = 0-h-.05
	base = sh
	color_list = ['red', 'blue', 'green', 'orange', 'brown']
	color_db = {}
	idx = 0
	for type in sorted(type_list):
		color_db[type] = color_list[idx]
		idx += 1
		type_offset[type] = base
		base += sh

	max_len = 0
	for chrn in chr_len:
		if max_len < chr_len[chrn]:
			max_len = chr_len[chrn]

	# Draw Line as Chromosomes and SVs
	y_ticks = []
	y_labels = []
	plt.figure(figsize=(10, 8), dpi=800)
	for i in range(y_cnt, 0, 0-f_cnt):
		chrn = chr_list[(y_cnt-i)/f_cnt]
		plt.plot([0, chr_len[chrn]], [i, i], color='black', lw=0.5, aa=False)
		plt.text(0-max_len/10, i-0.25, chrn, fontsize=10)
		cnt = 0
		for type in data_db[chrn]:
			cnt += 1
			for j in range(0, f_cnt):
				ft = f_list[j]
				y = i-j+type_offset[type]
				if cnt == int(len(type_list)/2):
					y_ticks.append(y)
					y_labels.append(ft)
				if ft not in data_db[chrn][type]:
					continue
				for x1, x2 in data_db[chrn][type][ft]:
					w = x2-x1+200000
					x = x1
					plt.gca().add_patch(plt.Rectangle((x, y), w, h, fill=True, facecolor=color_db[type], edgecolor=color_db[type], lw=0, aa=False))

	x_ticks = []
	x_labels = []
	for i in range(0, max_len, int(1e7)):
		x_ticks.append(i)
		x_labels.append(str(int(i/1e7)))
	#plt.yticks(range(f_cnt, y_cnt+1, f_cnt), chr_list[::-1])
	#plt.xticks(x_ticks, x_labels, fontsize=5)
	plt.yticks(y_ticks, y_labels, fontsize=5)
	plt.xlim(0, max_len)
	plt.ylim(0, y_cnt)
	ax = plt.gca()
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.tick_params(axis='x', direction='out', top='off')
	ax.tick_params(axis='y', which='both', left='off', right='off')
	
	for type in color_db:
		plt.scatter(0, 0, color=color_db[type], label=type, marker='s', s=0.1, alpha=1)

	plt.legend(fontsize=10, markerscale=15, loc=[1.01, 0.5], frameon=False, scatterpoints=1)
	
	plt.savefig(out_pic+'.pdf', filetype=out_pic.split('.')[-1], bbox_inches='tight')
	print("Finished")


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("Usage: python "+sys.argv[0]+" <in_dir> <chr_lens> <out_pic>")
	else:
		in_dir, chr_lens, out_pic = sys.argv[1:]
		plot_sv(in_dir, chr_lens, out_pic)
