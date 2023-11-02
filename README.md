# ArcheoNote - Automatic Annotation of Italian Archeological Reports

This repo contains the code and the trained model to annotate archelogical reports written in Italian.

This tool has been developed within the [Ariadne plus EU project](https://ariadne-infrastructure.eu/).

The main script is [``archeonote_annotate_it.py``](archeonote_annotate_it.py).

It takes in input a filename. The filename may point to a txt file a pdf file or a zip file containing many pdf and txt files.

The script produces as the output a zip file named ``output.zip`` containing an HTML file with the annotations for each input file.

[Screenshot](screenshot.png)

The file [``example_input_documents.zip``](example_input_documents.zip) is an example of input data.

See [``requirements.txt``](requirements.txt) for the requirements of the pdf environment.

See [LICENSE](LICENSE) file for the license terms.
