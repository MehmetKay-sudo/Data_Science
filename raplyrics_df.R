#first read data from txt file 
#read_data <- function(filepath) {
#  data <- read.tablee(filepath, header = TRUE, sep = "\t")
#}

# step 1 in reading a txt file 
read_text_file <- function(filepath) {
  file_data <- readLines(filepath)
  return(file_data)
}

# step 2 combine multiple txt files 
combine_txt_files <- function(data_dir) {
  all_data <. vectir(mode = "character", length = 0)   
}
