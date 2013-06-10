bac2012
=======

The results of BAC 2012. 

This data is freely available on the internet and you will not commit any crimes by downloading and working
with it.

The BAC or Bacalaureat is the final high-school exam in Romania. Each student is
expected to pass this exam after 4 years of high-school.

The exam has two phases:
  * Phase 1: The actual exam(s).
  * Phase 2: People that failed Phase 1 get a second chance to get their BAC Degree.
  
I wrote a small Python crawler to extract the data from a 3rd party webpage. I did not download
the Phase 2 results. The results are stored in CSV format (pipe '|' separated, CRLF EOL delimited), there is no
text qualifier.

The CSV file header is:
No|Name|Regional position|Country poistion|School Name|Previous Gradutate|Study type|specialization|RO-competency|RO-writing|RO-new-grade|RO-final-grade|NATIVE-competency|Modern-language|Modern-language-grade|Mandatory-study|Chosen-study|Digital-competency|Final-grade|Final-result|NATIVE-competency2|NATIVE-writing|NATIVE-new-grade|NATIVE-final-grade|Mandatory-study-grade|Mandatory-study-new-grade|Mandatory-study-final-grade|Chosen-study-grade|Chosen-study-new-grade|Chosen-study-final-grade

Have fun!



Known issues:
  * A line will repeat itself throughout the CSV file. I have not yet removed it. It's the HTML table header.
  
  nr.crt.|nume, initialatatalui,|pozitiain|pozitiain|unitatea deinvatamant|promotieanterioara|formainvatamant|specializare|limba si literatura romana|limba si literatura materna|limba modernastudiata -|nota|disciplina obligatorie aprofilului - scris|disciplina la alegere -scris|competentedigitale|media|rezultatulfinal|competente|scris|contestatie|notafinala|competente|scris|contestatie|notafinala|nota|contestatie|notafinala|nota|contestatie|notafinala
