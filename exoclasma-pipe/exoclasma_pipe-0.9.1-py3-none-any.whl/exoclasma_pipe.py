__scriptname__ = 'exoclasma-pipe'
__version__ = 'v0.9.1'

import argparse
import contextlib
import datetime
import functools
import glob
import io
import json
import logging
import multiprocessing
import os
import pandas #
import subprocess
import sys
import tempfile

G_FASTQC_MAXREADS = 1000000

# -----=====| LOGGING |=====-----

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)


# -----=====| DEPS |=====-----

def CheckDependency(Name):
	Shell = subprocess.Popen(Name, shell = True, executable = 'bash', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	Stdout, _ = Shell.communicate()
	if Shell.returncode == 127:
		logging.error(f'Dependency "{Name}" is not found!')
		exit(1)
	if Shell.returncode == 126:
		logging.error(f'Dependency "{Name}" is not executable!')
		exit(1)

def CheckDependencies():
	CheckDependency('fastqc -h')
	CheckDependency('cutadapt')
	CheckDependency('samtools')
	CheckDependency('bwa')
	CheckDependency('bedtools')
	CheckDependency('gatk')


# ------======| THREADING |======------

@contextlib.contextmanager
def Threading(Threads = multiprocessing.cpu_count()):
	pool = multiprocessing.Pool(Threads)
	yield pool
	pool.close()
	pool.join()
	del pool


# ------======| SUBPROCESS |======------

def BashSubprocess(SuccessMessage, Command):
	logging.debug(f'Shell command: {Command}')
	Shell = subprocess.Popen(Command, shell = True, executable = 'bash', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	_, Stderr = Shell.communicate()
	if (Shell.returncode != 0):
		logging.error(f'Shell command returned non-zero exit code {Shell.returncode}: {Command}\n{Stderr.decode("utf-8")}')
		exit(1)
	logging.info(SuccessMessage)


# ------======| MISC |======------

def MultipleTags(Tag, List, Quoted = True):
	Result = list()
	for Item in List:
		Result.append(Tag)
		Result.append(ArmorDoubleQuotes(Item) if Quoted else Item)
	return ' '.join(Result)

def ArmorDoubleQuotes(String): return f'"{String}"'

def ArmorSingleQuotes(String): return f"'{String}'"


# ------======| COVERAGE & ENRICHMENT STATS |======------

def LoadBedtoolsOutput(FN):
	return pandas.read_csv(FN, sep = '\t', header = None, dtype = {1: int, 4: float})[[1, 4]]

def CoverageStatsStage(Unit):
	with tempfile.TemporaryDirectory() as TempDir:
		CaptureTemp = os.path.join(TempDir, 'capture.csv')
		NotCaptureTemp = os.path.join(TempDir, 'not_capture.csv')
		CommandCaptureCoverage = ['bedtools', 'coverage', '-hist', '-sorted', '-g', ArmorDoubleQuotes(os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['samtools.faidx'])), '-a', ArmorDoubleQuotes(os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['capture'][Unit['Reference']['Capture']]['capture'])), '-b',  ArmorDoubleQuotes(os.path.join(Unit['OutputDir'], Unit['Output']['DuplessCoordBAM'])), '|', 'grep', '-P', ArmorDoubleQuotes(r'^all.*$'), '>', ArmorDoubleQuotes(CaptureTemp)]
		CommandNotCaptureCoverage = ['bedtools', 'coverage', '-hist', '-sorted', '-g', ArmorDoubleQuotes(os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['samtools.faidx'])), '-a', ArmorDoubleQuotes(os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['capture'][Unit['Reference']['Capture']]['not.capture'])), '-b',  ArmorDoubleQuotes(os.path.join(Unit['OutputDir'], Unit['Output']['DuplessCoordBAM'])), '|', 'grep', '-P', ArmorDoubleQuotes(r'^all.*$'), '>', ArmorDoubleQuotes(NotCaptureTemp)]
		BashSubprocess('Capture created', ' '.join(CommandCaptureCoverage))
		BashSubprocess('NotCapture created', ' '.join(CommandNotCaptureCoverage))
		CaptureData = LoadBedtoolsOutput(CaptureTemp)
		NotCaptureData = LoadBedtoolsOutput(NotCaptureTemp)
	Result = {
		'Capture DP>10 [%]':   CaptureData[CaptureData[1] >= 10][4].sum() * 100,
		'Capture Average':     CaptureData.apply(lambda x: x[1] * x[4], axis=1).sum(),
		'NotCapture Average':  NotCaptureData.apply(lambda x: x[1] * x[4], axis=1).sum(),
		'Enrichment Average':  None,
		'Capture DP0 [%]':     CaptureData.loc[0, 4] * 100,
		'NotCapture DP0 [%]':  NotCaptureData.loc[0, 4] * 100
	}
	try:
		Result['Enrichment Average'] = Result['Capture Average'] / Result['NotCapture Average']
	except ZeroDivisionError:
		pass
	Unit['Output']['CoverageStats'] = Result


# ------======| MARK DUPLICATES |======------

def GetActiveContigs(Unit):
	Data = [item for item in ''.join(open(os.path.join(Unit['OutputDir'], Unit['Output']['Contigs']), 'rt').readlines())[:-1].split('\n') if item != '*']
	SortedContigs = [item for item in Unit['Reference']['GenomeInfo']['chrom.sizes.dict'] if item in Data]
	return SortedContigs

def LoadMarkDuplicatesStat(StatTXT):
	Data = ''.join(open(StatTXT, 'rt').readlines())
	Stream = io.StringIO(Data.split('\n\n')[1])
	Table = pandas.read_csv(Stream, sep='\t', comment='#').set_index('LIBRARY')
	return Table.astype(object).transpose().to_dict()

def MarkDuplicates(InputBAM, OutputBAM, QuerySortedBAM, MarkDupMetrics, ActiveContigsFile, JavaOptions):
	ActiveContigsCommand = ['samtools', 'view', '-O', 'SAM', ArmorDoubleQuotes('/dev/stdin'), '|',
		'awk', '-F', ArmorSingleQuotes(r'\t'),  ArmorSingleQuotes(r'{ print $3 }'), '-', '|', 'sort', '|', 'uniq', '>', ArmorDoubleQuotes(ActiveContigsFile), ';']
	CommandMarkDuplicates = ['set', '-o', 'pipefail', ';',
		'gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['SortSam']), 'MarkDuplicates', '--REMOVE_DUPLICATES', 'false',
		'--ADD_PG_TAG_TO_READS',  'false', '--TAGGING_POLICY', 'All', '--ASSUME_SORT_ORDER', 'queryname',
		'-M',  ArmorDoubleQuotes(MarkDupMetrics), '-I', ArmorDoubleQuotes(InputBAM), '-O', ArmorDoubleQuotes(QuerySortedBAM)]
	CommandRemoveAndSort = ['samtools', 'view', '-h', '-F', '1024', ArmorDoubleQuotes(QuerySortedBAM), '|',
		'tee', '>('] + ActiveContigsCommand + [')', '|',
		'gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['SortSam']), 'SortSam', '--CREATE_INDEX', 'true', '-SO', 'coordinate', '-I', ArmorDoubleQuotes('/dev/stdin'), '-O', ArmorDoubleQuotes(OutputBAM)]
	BashSubprocess('MarkDuplicates finished', ' '.join(CommandMarkDuplicates))
	BashSubprocess('Dups removed', ' '.join(CommandRemoveAndSort))

def MarkDuplicatesStage(Unit):
	MarkDuplicates(
		InputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['PrimaryBAM']),
		OutputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['DuplessCoordBAM']),
		QuerySortedBAM = os.path.join(Unit['OutputDir'], Unit['Output']['DuplessQueryBAM']),
		MarkDupMetrics = os.path.join(Unit['OutputDir'], Unit['Output']['DuplessMetrics']),
		ActiveContigsFile = os.path.join(Unit['OutputDir'], Unit['Output']['Contigs']),
		JavaOptions = Unit['Config']['JavaOptions']
		)
	Unit['Output']['DuplessMetrics'] = LoadMarkDuplicatesStat(os.path.join(Unit['OutputDir'], Unit['Output']['DuplessMetrics']))
	Unit['Output']['Contigs'] = GetActiveContigs(Unit)


# ------======| ALIGN & MERGE BAM |======------

def FlagStat(InputBAM, SamtoolsFlagstats, Threads):
	Command = f'samtools flagstat -@ {Threads} -O json "{InputBAM}" > "{SamtoolsFlagstats}"'
	BashSubprocess('FlagStat ready', Command)

def RGTag(RG_Info):
	ID = f'D-{RG_Info["Instrument"]}.L-{RG_Info["Lane"]}'
	PL = RG_Info['Platform']
	PU = f'D-{RG_Info["Instrument"]}.L-{RG_Info["Lane"]}.BC-{RG_Info["Barcode"]}'
	LB = f'LIB-{RG_Info["Sample"]}-{RG_Info["Library"]}'
	SM = RG_Info['Sample']
	return f'@RG\\tID:{ID}\\tPL:{PL}\\tPU:{PU}\\tLB:{LB}\\tSM:{SM}'

def BWA(Mode, InputFastQ_R1, InputFastQ_R2, OutputBAM, RG_Header, ReferenceFASTA, JavaOptions, Threads):
	if Mode == 'Single-end':
		Command = ['set', '-o', 'pipefail', ';',
			'bwa', 'mem', '-R', ArmorDoubleQuotes(RG_Header), '-t', str(Threads), '-v', str(1), ArmorDoubleQuotes(ReferenceFASTA), ArmorDoubleQuotes(InputFastQ_R1), '|',
			'gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['SortSam']), 'SortSam', '-SO', 'queryname', '-I', ArmorDoubleQuotes('/dev/stdin'), '-O', ArmorDoubleQuotes(OutputBAM)]
	if Mode == 'Paired-end':
		Command = ['set', '-o', 'pipefail', ';',
			'bwa', 'mem', '-R', ArmorDoubleQuotes(RG_Header), '-t', str(Threads), '-v', str(1),  ArmorDoubleQuotes(ReferenceFASTA), ArmorDoubleQuotes(InputFastQ_R1), ArmorDoubleQuotes(InputFastQ_R2), '|',
			'gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['SortSam']), 'SortSam', '-SO', 'queryname', '-I', ArmorDoubleQuotes('/dev/stdin'), '-O', ArmorDoubleQuotes(OutputBAM)]
	BashSubprocess('BWA finished', ' '.join(Command))

def MergeSamFiles(BAM_List, OutputBAM, SortOrder):
	TaggedBAMs = MultipleTags('-I', BAM_List)
	Command = ['gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['MergeSamFiles']), 'MergeSamFiles', '--USE_THREADING', 'true', '-SO', SortOrder, TaggedBAMs, '-O', ArmorDoubleQuotes(OutputBAM)]
	BashSubprocess('BAM files merged', ' '.join(Command))

def BWAStage(Unit):
	with tempfile.TemporaryDirectory() as TempDir:
		Shards = []
		for Index, Item in enumerate(Unit['Input']):
			StrIndex = str(Index)
			RG = RGTag(Item['RG'])
			if Item['Adapter'] is not None:
				R1 = None if Unit['Output']['Cutadapt'][StrIndex]['CutadaptR1'] is None else os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['CutadaptR1'])
				R2 = None if Unit['Output']['Cutadapt'][StrIndex]['CutadaptR2'] is None else os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['CutadaptR2'])
				Unpaired = None if Unit['Output']['Cutadapt'][StrIndex]['CutadaptUnpaired'] is None else os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['CutadaptUnpaired'])
			else:
				R1 = Item['Files']['R1']
				R2 = Item['Files']['R2']
				Unpaired = Item['Files']['Unpaired']
			if Unpaired is not None:
				OutputBAM = os.path.join(TempDir, f'temp_{StrIndex}_unpaired.bam')
				BWA(
					Mode = 'Single-end',
					InputFastQ_R1 = Unpaired,
					InputFastQ_R2 = None,
					ReferenceFASTA = os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['fasta']),
					RG_Header = RG,
					OutputBAM = OutputBAM,
					JavaOptions = Unit['Config']['JavaOptions'],
					Threads = Unit['Config']['Threads']
					)
				Shards.append(OutputBAM)
			if (R1 is not None) and (R2 is not None):
				OutputBAM = os.path.join(TempDir, f'temp_{StrIndex}_paired.bam')
				BWA(
					Mode = 'Paired-end',
					InputFastQ_R1 = R1,
					InputFastQ_R2 = R2,
					ReferenceFASTA = os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['fasta']),
					RG_Header = RG,
					OutputBAM = OutputBAM,
					JavaOptions = Unit['Config']['JavaOptions'],
					Threads = Unit['Config']['Threads']
					)
				Shards.append(OutputBAM)
		if len(Shards) > 1:
			MergeSamFiles(
				BAM_List = Shards,
				OutputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['PrimaryBAM']),
				SortOrder = 'queryname'
				)
		else:
			CommandMove = ['mv', ArmorDoubleQuotes(Shards[0]), ArmorDoubleQuotes(os.path.join(Unit['OutputDir'], Unit['Output']['PrimaryBAM']))]
			BashSubprocess('BAM moved', ' '.join(CommandMove))
		FlagStat(
			InputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['PrimaryBAM']),
			SamtoolsFlagstats = os.path.join(Unit['OutputDir'], Unit['Output']['FlagStat']),
			Threads = Unit['Config']['Threads']
			)
		Unit['Output']['FlagStat'] = json.load(open(os.path.join(Unit['OutputDir'], Unit['Output']['FlagStat']), 'rt'))


# ------======| CUTADAPT |======------

def Cutadapt(InputFastQ_R1, OutputFastQ_R1, InputFastQ_R2, OutputFastQ_R2, CutadaptReport, Adapter, Mode, Threads):
	if Mode == 'Single-end':
		Command = ['cutadapt', '--report', 'minimal', '-j', str(Threads), '-e', str(0.2), '-m', str(8), '-a', Adapter['R1'], '-o',
			ArmorDoubleQuotes(OutputFastQ_R1), ArmorDoubleQuotes(InputFastQ_R1), '>', ArmorDoubleQuotes(CutadaptReport)]
	if Mode == 'Paired-end':
		Command = ['cutadapt', '--report', 'minimal', '-j', str(Threads), '-e', str(0.2), '-m', str(8), '-a', Adapter['R1'], '-A', Adapter['R2'],
			 '-o',  ArmorDoubleQuotes(OutputFastQ_R1), '-p', ArmorDoubleQuotes(OutputFastQ_R2), ArmorDoubleQuotes(InputFastQ_R1), ArmorDoubleQuotes(InputFastQ_R2),
			 '>', ArmorDoubleQuotes(CutadaptReport)]
	BashSubprocess('Cutadapt finished', ' '.join(Command))

def CutadaptStage(Unit):
	for Index, Item in enumerate(Unit['Input']):
		StrIndex = str(Index)
		if Item['Adapter'] is not None:
			if Item['Files']['Unpaired'] is not None:
				Cutadapt(
					Mode = 'Single-end',
					InputFastQ_R1 = Item['Files']['Unpaired'],
					InputFastQ_R2 = None,
					OutputFastQ_R1 = os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['CutadaptUnpaired']),
					OutputFastQ_R2 = None,
					Adapter = Item['Adapter'],
					CutadaptReport = os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['StatsUnpaired']),
					Threads = Unit['Config']['Threads']
					)
				FileToAnalyze = Unit['Output']['Cutadapt'][StrIndex]['CutadaptUnpaired']
				Unit['Output']['Cutadapt'][StrIndex]['StatsUnpaired'] = CutadaptStat(os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['StatsUnpaired']))
			else:
				Unit['Output']['Cutadapt'][StrIndex]['CutadaptUnpaired'] = None
				Unit['Output']['Cutadapt'][StrIndex]['StatsUnpaired'] = None
			if (Item['Files']['R1'] is not None) and (Item['Files']['R2'] is not None):
				Cutadapt(
					Mode = 'Paired-end',
					InputFastQ_R1 = Item['Files']['R1'],
					InputFastQ_R2 = Item['Files']['R2'],
					OutputFastQ_R1 = os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['CutadaptR1']),
					OutputFastQ_R2 = os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['CutadaptR2']),
					Adapter = Item['Adapter'],
					CutadaptReport = os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['StatsPaired']),
					Threads = Unit['Config']['Threads']
					)
				FileToAnalyze = Unit['Output']['Cutadapt'][StrIndex]['CutadaptR1']
				Unit['Output']['Cutadapt'][StrIndex]['StatsPaired'] = CutadaptStat(os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['StatsPaired']))
			else:
				Unit['Output']['Cutadapt'][StrIndex]['CutadaptR1'] = None
				Unit['Output']['Cutadapt'][StrIndex]['CutadaptR2'] = None
				Unit['Output']['Cutadapt'][StrIndex]['StatsPaired'] = None
			FastQC(
				InputFastQ = os.path.join(Unit['OutputDir'], FileToAnalyze),
				OutputHTML = os.path.join(Unit['OutputDir'], Unit['Output']['Cutadapt'][StrIndex]['FastQC'])
				)

def CutadaptStat(StatTXT):
	Data = pandas.read_csv(StatTXT, sep = '\t')
	return Data.transpose()[0].to_dict()


# ------======| FILENAMES |======------

def GenerateAlignFileNames(Unit):
	ID = Unit['ID']
	FileNames = {
		'PrimaryBAM':       f'_temp.{ID}.primary.bam',
		'FlagStat':         f'_temp.{ID}.flagstat.json',
		'DuplessCoordBAM':  f'{ID}.coordinate_sorted.bam',
		'DuplessQueryBAM':  f'{ID}.query_sorted.bam',
		'DuplessMetrics':   f'_temp.{ID}.md_metrics.txt',
		'CoverageStats':    f'_temp.{ID}.coverage.json',
		'Contigs':          f'_temp.{ID}.contigs.txt'
	}
	FileNames['Cutadapt'] = { str(index): {
		'CutadaptR1':       f'_temp.{ID}.{index}.R1.cutadapt.fastq.gz',
		'CutadaptR2':       f'_temp.{ID}.{index}.R2.cutadapt.fastq.gz',
		'CutadaptUnpaired': f'_temp.{ID}.{index}.unpaired.cutadapt.fastq.gz',
		'StatsUnpaired':    f'_temp.{ID}.{index}.cutadapt_unpaired_stats.tsv',
		'StatsPaired':      f'_temp.{ID}.{index}.cutadapt_paired_stats.tsv',
		'FastQC':           f'{ID}.{index}.fastqc.html'
		} for index in range(len(Unit['Input'])) }
	return FileNames


# ------======| REMOVE TEMP FILES |======------

def RemoveStage(Unit):
	TempFiles = [ArmorDoubleQuotes(File) for File in glob.glob(os.path.join(Unit['OutputDir'], '_temp.*'))]
	Command = ['rm'] + TempFiles
	BashSubprocess('Files removed', ' '.join(Command))


# -----=====| FASTQC |=====-----

def FastQC(InputFastQ, OutputHTML, Size = G_FASTQC_MAXREADS, Threads = multiprocessing.cpu_count()):
	with tempfile.TemporaryDirectory() as TempDir:
		FastQRealPath = os.path.realpath(InputFastQ)
		HTMLRealPath = os.path.realpath(OutputHTML)
		AnalyzeFilename = FastQRealPath
		if Size != 0:
			SampleFilename = os.path.join(TempDir, "sample.fastq.gz")
			BashSubprocess(f'FastQ subsampled: "{FastQRealPath}"', f'zcat -q "{FastQRealPath}" | head -{str(Size * 4)} | gzip -c > "{SampleFilename}"')
			AnalyzeFilename = SampleFilename
		BashSubprocess(f'FastQ analyzed: "{FastQRealPath}"', f'fastqc -o "{TempDir}" -t {str(Threads)} "{AnalyzeFilename}"')
		HTMLTemp = glob.glob(os.path.join(TempDir, "*.html"))
		if len(HTMLTemp) != 1:
			logging.error(f'Error processing file "{FastQRealPath}"')
			exit(1)
		BashSubprocess(f'Report copied: "{HTMLRealPath}"', f'cp "{HTMLTemp[0]}" "{HTMLRealPath}"')


## ------======| BQSR |======------

def ContigBaseRecalibration(Contig, InputBAM, dbSNP, TempDirectory, ReferenceFASTA, JavaOptions):
	BQSRTable = os.path.join(TempDirectory, f'bqsr_table_{Contig}.tsv')
	OutputBAM = os.path.join(TempDirectory, f'output_{Contig}.bam')
	CommandBaseRecalibrator = ['gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['BaseRecalibrator']), 'BaseRecalibrator', '-L', Contig, '-I', ArmorDoubleQuotes(InputBAM), '--known-sites',  ArmorDoubleQuotes(dbSNP), '-O', ArmorDoubleQuotes(BQSRTable), '-R', ArmorDoubleQuotes(ReferenceFASTA)]
	CommandApplyBQSR = ['gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['ApplyBQSR']), 'ApplyBQSR', '-OBI', 'false', '-L', Contig, '-bqsr', ArmorDoubleQuotes(BQSRTable), '-I', ArmorDoubleQuotes(InputBAM),  '-O', ArmorDoubleQuotes(OutputBAM)]
	BashSubprocess(f'Base recalibration, recalibration of {Contig} finished', ' '.join(CommandBaseRecalibrator))
	BashSubprocess(f'Base recalibration, apply of {Contig} finished', ' '.join(CommandApplyBQSR))
	return OutputBAM

def BaseRecalibration(InputBAM, OutputBAM, ActiveContigs, dbSNP, JavaOptions, ReferenceFASTA, Threads):
	with tempfile.TemporaryDirectory() as TempDir:
		with Threading(Threads) as pool:
			Shards = pool.map(functools.partial(ContigBaseRecalibration, InputBAM = InputBAM, TempDirectory = TempDir, dbSNP = dbSNP, ReferenceFASTA = ReferenceFASTA, JavaOptions = JavaOptions), ActiveContigs)
			TaggedShards = MultipleTags('-I', Shards, Quoted = True)
		CommandMergeSamFiles = ['gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['MergeSamFiles']), 'MergeSamFiles', '--CREATE_INDEX', 'true', '-SO', 'coordinate',  TaggedShards, '-O', ArmorDoubleQuotes(OutputBAM)]
		BashSubprocess('BAM files merged', ' '.join(CommandMergeSamFiles))

def BaseRecalibrationStage(Unit):
	BaseRecalibration(
		InputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['DuplessCoordBAM']),
		OutputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['RecalibratedBAM']),
		ActiveContigs = Unit['Output']['Contigs'],
		dbSNP = Unit['Reference']['BQSR_dbSNP'],
		JavaOptions = Unit['Config']['JavaOptions'],
		ReferenceFASTA = os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['fasta']),
		Threads = Unit['Config']['Threads']
		)

## ------======| VARIANT CALLING |======------

def ContigHaplotypeCalling(Contig, InputBAM, ReferenceFASTA, JavaOptions, TempDirectory):
	OutputGVCF = os.path.join(TempDirectory, f'output_{Contig}.g.vcf.gz')
	OutputVCF = os.path.join(TempDirectory, f'output_{Contig}.vcf.gz')
	CommandHaplotypeCaller = ['gatk', '--java-options',  ArmorDoubleQuotes(JavaOptions['HaplotypeCaller']), 'HaplotypeCaller', '-OVI', 'true', '--native-pair-hmm-threads', str(2), '--dont-use-soft-clipped-bases', 'true', '-ERC', 'GVCF', '-L', Contig, '-I', ArmorDoubleQuotes(InputBAM), '-O', ArmorDoubleQuotes(OutputGVCF), '-R', ArmorDoubleQuotes(ReferenceFASTA)]
	CommandGenotypeGVCFs = ['gatk', '--java-options', ArmorDoubleQuotes(JavaOptions['GenotypeGVCFs']), 'GenotypeGVCFs', '-L', Contig, '-V', ArmorDoubleQuotes(OutputGVCF), '-O', ArmorDoubleQuotes(OutputVCF), '-R', ArmorDoubleQuotes(ReferenceFASTA)]
	BashSubprocess(f'HaplotypeCalling, gVCF {Contig} ready', ' '.join(CommandHaplotypeCaller))
	BashSubprocess(f'HaplotypeCalling, VCF {Contig} ready', ' '.join(CommandGenotypeGVCFs))
	return { 'VCF': OutputVCF, 'gVCF': OutputGVCF }

def HaplotypeCalling(InputBAM, ActiveContigs, Output_VCF, Output_gVCF, JavaOptions, ReferenceFASTA, Threads):
	with tempfile.TemporaryDirectory() as TempDir:
		with Threading(Threads) as pool:
			Shards = pool.map(functools.partial(ContigHaplotypeCalling, InputBAM = InputBAM, TempDirectory = TempDir, JavaOptions = JavaOptions, ReferenceFASTA = ReferenceFASTA), ActiveContigs)
			TaggedShardsVCF = MultipleTags('-I', [item['VCF'] for item in Shards], Quoted = True)
			TaggedShardsGVCF = MultipleTags('-I', [item['gVCF'] for item in Shards], Quoted = True)
		CommandMergeVcfs = ['gatk', '--java-options',  ArmorDoubleQuotes(JavaOptions['MergeVcfs']), 'MergeVcfs', '--CREATE_INDEX', 'true', TaggedShardsVCF, '-O', ArmorDoubleQuotes(Output_VCF)]
		CommandMergeGVcfs = ['gatk', '--java-options',  ArmorDoubleQuotes(JavaOptions['MergeVcfs']), 'MergeVcfs', '--CREATE_INDEX', 'true', TaggedShardsGVCF, '-O', ArmorDoubleQuotes(Output_gVCF)]
		BashSubprocess('VCF merged', ' '.join(CommandMergeVcfs))
		BashSubprocess('gVCF merged', ' '.join(CommandMergeGVcfs))

def HaplotypeCallingStage(Unit):
	HaplotypeCalling(
		InputBAM = os.path.join(Unit['OutputDir'], Unit['Output']['RecalibratedBAM']),
		ActiveContigs = Unit['Output']['Contigs'],
		Output_VCF = os.path.join(Unit['OutputDir'], Unit['Output']['VCF']),
		Output_gVCF = os.path.join(Unit['OutputDir'], Unit['Output']['gVCF']),
		JavaOptions = Unit['Config']['JavaOptions'],
		ReferenceFASTA = os.path.join(Unit['Reference']['GenomeDir'], Unit['Reference']['GenomeInfo']['fasta']),
		Threads = Unit['Config']['Threads']
		)


# -----=====| COMMAND FUNC |=====-----

def PrimaryFastqAnalysis(Files, OutputDir, Size = G_FASTQC_MAXREADS, Threads = multiprocessing.cpu_count()):
	logging.info(f'{__scriptname__} FastQC {__version__}')
	OutputDirRealPath = os.path.realpath(OutputDir)
	os.mkdir(OutputDirRealPath)
	FilesFullList = list()
	for File in Files: FilesFullList += glob.glob(File)
	FilesFullList = list(set([os.path.realpath(File) for File in FilesFullList]))
	for Index, File in enumerate(FilesFullList):
		ReportRealPath = os.path.join(OutputDirRealPath, f'{Index}_{os.path.basename(File)}_FastQCReport.html')
		FastQC(InputFastQ = File, OutputHTML = ReportRealPath, Size = Size, Threads = Threads)
	logging.info('Job finished')

def AlignPipeline(UnitFile):
	logging.info(f'{__scriptname__} Align {__version__}')
	ConfigPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
	UnitPath = os.path.realpath(UnitFile)
	Config = json.load(open(ConfigPath, 'rt'))
	Unit = json.load(open(UnitPath, 'rt'))
	logging.info(f'Unit loaded: "{UnitPath}"')
	try:
		Unit['ParentDir'] = os.path.realpath(Unit['ParentDir'])
		Unit['Started'] = datetime.datetime.now().isoformat()
		Unit['OutputDir'] = os.path.join(Unit['ParentDir'], Unit['ID'])
		UnitJson = os.path.join(Unit['OutputDir'], 'unit.json')
		os.mkdir(Unit['OutputDir'])
		Unit['Output'] = GenerateAlignFileNames(Unit)
		for Index in range(len(Unit['Input'])):
			for Type in Unit['Input'][Index]['Files']:
				Unit['Input'][Index]['Files'][Type] = None if Unit['Input'][Index]['Files'][Type] is None else os.path.realpath(Unit['Input'][Index]['Files'][Type])
			if Unit['Input'][Index]['Adapter'] is not None:
				Unit['Input'][Index]['Adapter'] = Config['Adapters'][Unit['Input'][Index]['Adapter']]
		Unit['Config']['JavaOptions'] = Config['JavaOptions']
		Unit['Reference']['GenomeDir'] = os.path.realpath(os.path.dirname(Unit['Reference']['GenomeInfo']))
		Unit['Reference']['GenomeInfo'] = json.load(open(Unit['Reference']['GenomeInfo'], 'rt'))
		Unit['Stage'] = list()
		json.dump(Unit, open(UnitJson, 'wt'), indent = 4, ensure_ascii = False)
	except FileExistsError:
		logging.warning('Load previously started pipeline')
		Unit = json.load(open(UnitJson, 'rt'))
	StageAlias = 'Cutadapt'
	if StageAlias not in Unit['Stage']:
		CutadaptStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitJson, 'wt'), indent = 4, ensure_ascii = False)
	StageAlias = 'BWA'
	if StageAlias not in Unit['Stage']:
		BWAStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitJson, 'wt'), indent = 4, ensure_ascii = False)
	StageAlias = 'MarkDuplicates'
	if StageAlias not in Unit['Stage']:
		MarkDuplicatesStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitJson, 'wt'), indent = 4, ensure_ascii = False)
	StageAlias = 'CoverageStats'
	if (StageAlias not in Unit['Stage']) and (Unit['Reference']['Capture'] is not None):
		CoverageStatsStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitJson, 'wt'), indent = 4, ensure_ascii = False)
	StageAlias = 'RemoveTempFiles'
	if (StageAlias not in Unit['Stage']) and Unit['Config']['RemoveTempFiles']:
		RemoveStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitJson, 'wt'), indent = 4, ensure_ascii = False)
	logging.info('Job finished')

def CallPipeline(Units, dbSNP):
	logging.info(f'{__scriptname__} Call {__version__}')
	UnitPath = os.path.realpath(Units)
	Unit = json.load(open(UnitPath, 'rt'))
	logging.info(f'Unit loaded: "{UnitPath}"')
	Unit['Output']['RecalibratedBAM'] = f'_temp.{Unit["ID"]}.recalibrated.bam'
	Unit['Output']['VCF'] = f'{Unit["ID"]}.vcf.gz'
	Unit['Output']['gVCF'] = f'{Unit["ID"]}.g.vcf.gz'
	Unit['Reference']['BQSR_dbSNP'] = os.path.realpath(dbSNP)
	StageAlias = 'BaseRecalibration'
	if StageAlias not in Unit['Stage']:
		BaseRecalibrationStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitPath, 'wt'), indent = 4, ensure_ascii = False)
	StageAlias = 'HaplotypeCalling'
	if StageAlias not in Unit['Stage']:
		HaplotypeCallingStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitPath, 'wt'), indent = 4, ensure_ascii = False)
	StageAlias = 'RemoveTempFiles2'
	if (StageAlias not in Unit['Stage']) and Unit['Config']['RemoveTempFiles']:
		RemoveStage(Unit)
		Unit['Stage'].append(StageAlias)
		json.dump(Unit, open(UnitPath, 'wt'), indent = 4, ensure_ascii = False)
	logging.info('Job finished')


# -----=====| PARSER |=====-----

def CreateParser():
	Parser = argparse.ArgumentParser(
		formatter_class = argparse.RawDescriptionHelpFormatter,
		description = f'{__scriptname__}: Exo-C Data Quality Check, Mapping, and Variant Calling, part of ExoClasma Suite'
		)
	Parser.add_argument('-v', '--version', action = 'version', version = __version__)
	Subparsers = Parser.add_subparsers(title = 'Commands', dest = 'command')

	FastQCParser = Subparsers.add_parser('FastQC', help = f'FastQC wrapper for a pool of subsamples')
	FastQCParser.add_argument('-f', '--fastq', required = True, type = str, nargs = '+', help = f'Raw FASTQ files. May be gzipped or bzipped')
	FastQCParser.add_argument('-d', '--dir', required = True, type = str, help = f'Directory to write reports in')

	AlignParser = Subparsers.add_parser('Align', help = f'Align, sort and dedup reads')
	AlignParser.add_argument('-u', '--unit', required = True, type = str, help = f'Primary JSON unit file')

	CallParser = Subparsers.add_parser('Call', help = f'Recalibrate quals and call variants')
	CallParser.add_argument('-u', '--unit', required = True, type = str, help = f'Secondary JSON unit file')
	CallParser.add_argument('-d', '--dbsnp', required = True, type = str, help = f'dbSNP path (for BQSR)')
	return Parser


# -----=====| MAIN |=====-----

def main():
	Parser = CreateParser()
	Namespace = Parser.parse_args(sys.argv[1:])
	CheckDependencies()
	if Namespace.command == 'FastQC':
		Fastqs = Namespace.fastq
		OutputDir = Namespace.dir
		PrimaryFastqAnalysis(Fastqs, OutputDir)
	elif Namespace.command == 'Align':
		Units = Namespace.unit
		AlignPipeline(Units)
	elif Namespace.command == 'Call':
		Units = Namespace.unit
		dbSNP = Namespace.dbsnp
		CallPipeline(Units, dbSNP)
	else: Parser.print_help()


if __name__ == '__main__': main()
