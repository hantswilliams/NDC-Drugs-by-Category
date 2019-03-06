<h1> <bold> NDC Drug Categories </bold> </h1>
<br>
Mapping of U.S. Food and Drug Administration (FDA) National Drug Codes (NDC) to Anatomical Therapeutic Chemical (ATC) Level 4 classes
<br>
This script reads a file called _NDC_MASTER_INFO.csv_ with the following columns:  
**"YEAR", "MONTH", "NDC"**  
and outputs a file called _ndc_atc_long_list.csv_ containing the following columns:  
**"YEAR", "MONTH", "NDC", "RXCUI", "ATC4"**  
as well as another file called atc_name.csv with the following columns:  
**"ATC4", "ATC4_NAME"** 