    # Modifed by Mahmood Mortazavi Dehkordi 

    lines = spark.read.text("").rdd   # This line will be replaced with the configuration management
    parts = lines.map(lambda row: row.value.split(','))
    #field projection
    productsOnly = parts.filter(lambda p: p[1][0:5].isdigit())
    #filter empty customer records
    cleanData = productsOnly.filter(lambda p: p[6].isdigit())
    ratingsRDD = cleanData.map(lambda p: Row(customerId=int(p[6]), \
        itemId=int(p[1][0:5]), rating=1.0))