library(tximport)
library(DESeq2)
library(biomaRt)
library(fda)
dir = file.path(getwd(), "RNASeq/PRJNA406930/")
project_name = unlist(strsplit(dir, "/"))
project_name = project_name[length(project_name)]
samples = dirs(dir)
files <- file.path(dir, samples,"kallisto_output","abundance.h5")
files
names(files) = samples
# sampleTable = read.csv("./hiseq_info.txt", sep = "\t")
mart <- biomaRt::useMart(biomart = "plants_mart",
                          dataset = "athaliana_eg_gene",
                          host = 'plants.ensembl.org')
t2g <- biomaRt::getBM(attributes = c("ensembl_transcript_id", "ensembl_gene_id",
                                    "external_gene_name"), mart = mart)
t2g <- dplyr::rename(t2g, target_id = ensembl_transcript_id,
                      ens_gene = ensembl_gene_id, ext_gene = external_gene_name)
tx2gn = t2g[,1:2]

txi.kallisto <- tximport(files, type = "kallisto", tx2gene = tx2gn)
head(txi.kallisto$counts)
count = txi.kallisto$counts
#library(ComplexHeatmap)
#Heatmap(t(count))
write.csv(txi.kallisto$counts, paste0("./RNASeq/",project_name,"/",project_name,"_countfile.csv"))
