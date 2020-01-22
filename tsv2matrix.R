setwd("/media/rachel/Part2/OneDrive - south.du.ac.in/project_jnu/GRN/GRN_data/PRJNA315570_abundance/")
sras = list.files(path = ".", pattern = ".tsv")
sra_rows = read.csv(sras[1], stringsAsFactors = F, sep = "\t")
sra_rows = data.frame(sra_rows[order(sra_rows$target_id, decreasing = F),1])
colnames(sra_rows) = "gene_names"
col_sra = unlist(strsplit(sras,".tsv"))
#col_sra = col_sra[seq(1,length(col_sra),2)]
fpkm_df = matrix(NA, ncol = length(sras),nrow = nrow(sra_rows))
colnames(fpkm_df) = col_sra
rownames(fpkm_df) = sra_rows$gene_names
project_name = unlist(strsplit(getwd(),"/"))
project_name = project_name[length(project_name)]
project_name = unlist(strsplit(project_name,"_"))[1]
project_name = paste(project_name,".csv", sep = "")
i=1
for (i in 2:length(col_sra)) {
  ci = read.csv(sras[i], stringsAsFactors = F,sep = "\t")
  ci = data.frame(ci[order(ci$target_id, decreasing = F),])
  #colnames(ci) = c("names", "fpkm")
  fpkm_df[,i] = ci[match(ci$target_id, rownames(fpkm_df)),5]
}
write.csv(fpkm_df, file = project_name)
