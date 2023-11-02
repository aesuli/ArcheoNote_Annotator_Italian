html_template = '''<!DOCTYPE html><html><head><meta charset="utf-8">
    <title>ArcheoNote ISTI-CNR</title>
    <style>
    body {{
        margin: 0;
    }}
    .header {{
      width: 100%;
      background-color: gray;
      color: white;
      padding-top:5px;
      padding-bottom:5px;
      text-align: center;
    }}
    .footer {{
      position: fixed;
      left: 0;
      bottom: 0;
      width: 100%;
      background-color: gray;
      color: white;
      padding-top:5px;
      padding-bottom:5px;
      text-align: center;
    }}
    .annotation {{
     color: black;
     padding: 5px;
    }}
    .content {{
    padding: 20px;
    padding-bottom: 20%;
    }}
    .right {{
    float:right;
    margin-right:20px;
    }}
    .ARTEFACT {{
      background-color:#FF80BF;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .BIOLOGICALREMAIN {{
      background-color:#99bb22;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .COLOUR {{
      background-color:#99FF00;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .MATERIAL {{
      background-color:#33FFFF;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .PERIOD {{
      background-color:#3333FF;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .PERSON {{
      background-color:#009800;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .PLACE {{
      background-color:#FF6600;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .SITE {{
      background-color:#FFFF33;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .TECHNIQUE {{
      background-color:#A64DFF;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
    .TIMESPAN {{
      background-color:#FF0000;
      opacity: 0.8;
      filter: alpha(opacity=80); /* For IE8 and earlier */
    }}
</style>
</head>
<body>{}</body></html>'''