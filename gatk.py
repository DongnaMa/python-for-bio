import argparse
import subprocess

def GATK(reference,read1,read2,num_threads):
    route = '~/software/bin/'
    name = read1.replace('.fq.gz', '')
    cmd1 = 'bwa index '+ reference
    subprocess.call(cmd1, shell=True)
    cmd2 = 'java -jar '+route+'picard.jar CreateSequenceDictionary R='+reference+' O='+reference+'.dict'
    subprocess.call(cmd2, shell=True)
    cmd3 = 'samtools faidx '+reference
    subprocess.call(cmd3, shell=True)
    cmd4 = 'bwa mem -t '+str(num_threads)+' -R "@RG\\tID:<ID>\\tLB:<LIBRARY_'+name+'>\\tSM:<'+name+'>\\tPL:ILLUMINA" '+reference+'\t'+read1+'\t'+read2+' | samtools view -bS > '+name+'.bam'
    subprocess.call(cmd4, shell=True)
    cmd5 = 'java -jar '+route+'picard.jar SortSam I='+name+'.bam O='+name+'.sort.bam SORT_ORDER=coordinate'
    subprocess.call(cmd5, shell=True)
    cmd6 = 'java -jar '+route+'picard.jar AddOrReplaceReadGroups I='+name+'.sort.bam O='+name+'.sort.addhead.bam ID='+name+'ID LB='+name+'ID PL=illumina PU='+name+'PU SM='+name
    subprocess.call(cmd6, shell=True)
    cmd7 = 'java  -Xmx15g -jar '+route+'picard.jar MarkDuplicates I='+name+'.sort.addhead.bam O='+name+'.rmdup.bam REMOVE_DUPLICATES=false  MAX_FILE_HANDLES_FOR_READ_ENDS_MAP=1000 METRICS_FILE='+name+'.sort.addhead.bam.metrics'
    subprocess.call(cmd7, shell=True)
    cmd8 = 'samtools index '+name+'.rmdup.bam'
    subprocess.call(cmd8, shell=True)
    cmd9 = 'java -Xmx50g -jar '+route+'GenomeAnalysisTK.jar -R '+reference+' -T RealignerTargetCreator -I '+name+'.rmdup.bam -o '+name+'.realign.intervals '
    subprocess.call(cmd9, shell=True)
    cmd10 = 'java -Xmx50g -jar '+route+'GenomeAnalysisTK.jar -R '+reference+' -T IndelRealigner -targetIntervals '+name+'.realign.intervals -I '+name+'.rmdup.bam -o '+name+'.realign.bam '
    subprocess.call(cmd10, shell=True)
    cmd11 = 'java -Xmx50g -jar '+route+'GenomeAnalysisTK.jar -R '+reference+' -T HaplotypeCaller -I '+name+'.realign.bam -o '+name+'.gatk.raw.vcf -stand_call_conf 30 -nt '+str(num_threads)
    subprocess.call(cmd11, shell=True)

def main():
    parser = argparse.ArgumentParser(description='This script is using GATK call SNP')
    parser.add_argument('-f', '--reference', type=str, metavar='', required=True, help='reference fasta')
    parser.add_argument('-r1', '--read1', type=str, metavar='', required=True)
    parser.add_argument('-r2', '--read2', type=str, metavar='', required=True)
    parser.add_argument('-num_threads', '-num_threads', type=int, metavar='', help='number of threads[1]', default=1)
    args = parser.parse_args()
    GATK(args.reference, args.read1, args.read2, args.num_threads)


if __name__ == "__main__":
    main()