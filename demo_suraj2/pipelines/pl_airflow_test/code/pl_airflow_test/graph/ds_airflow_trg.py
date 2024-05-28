from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_test.config.ConfigStore import *
from pl_airflow_test.udfs.UDFs import *

def ds_airflow_trg(spark: SparkSession, in0: DataFrame):
    from typing import Optional, List, Dict
    from dataclasses import dataclass, field
    from abc import ABC
    
    from pyspark.sql.column import Column
    from pyspark.sql.functions import col
    from dataclasses import dataclass
    from typing import Optional, List, Dict
    from pyspark.sql.column import Column as sparkColumn


    @dataclass(frozen = True)
    class SColumn:
        expression: Optional[Column] = None

        @staticmethod
        def getSColumn(column: str):
            return SColumn(col(column))

        def column(self) -> sparkColumn:
            return self.expression

        def columnName(self) -> str:
            return self.expression._jc.toString()


    @dataclass(frozen = True)
    class SColumnExpression:
        target: str
        expression: SColumn
        description: str
        _row_id: Optional[str] = None

        @staticmethod
        def remove_backticks(s):
            if s.startswith("`") and s.endswith("`"):
                return s[1:- 1]
            else:
                return s

        @staticmethod
        def getColumnExpression(column: str):
            return SColumnExpression(column, SColumn.getSColumn(col(column)), "")

        @staticmethod
        def getColumnsFromColumnExpressionList(columnExpressions: list):
            columnList = []

            for expression in columnExpressions:
                columnList.append(expression.expression)

            return columnList

        def column(self) -> Column:

            if (self.expression.columnName() == SColumnExpression.remove_backticks(self.target)):
                return self.expression.expression

            return self.expression.expression.alias(self.target)


    @dataclass(frozen = True)
    class CsvProperties(DatasetProperties):
        schema: Optional[StructType] = None
        description: Optional[str] = ""
        useSchema: Optional[bool] = True
        path: str = ""
        separator: Optional[str] = str(",")
        encoding: Optional[str] = None
        quote: Optional[str] = None
        escape: Optional[str] = None
        charToEscapeQuoteEscaping: Optional[str] = None
        header: Optional[bool] = True
        ignoreLeadingWhiteSpaceReading: Optional[bool] = None
        ignoreTrailingWhiteSpaceReading: Optional[bool] = None
        ignoreLeadingWhiteSpaceWriting: Optional[bool] = None
        ignoreTrailingWhiteSpaceWriting: Optional[bool] = None
        nullValue: Optional[str] = None
        emptyValue: Optional[str] = None
        dateFormat: Optional[str] = None
        timestampFormat: Optional[str] = None
        comment: Optional[str] = None
        enforceSchema: Optional[bool] = None
        inferSchema: Optional[bool] = None
        samplingRatio: Optional[SFloat] = None
        nanValue: Optional[str] = None
        positiveInf: Optional[str] = None
        negativeInf: Optional[str] = None
        maxColumns: Optional[str] = None
        maxCharsPerColumn: Optional[str] = None
        unescapedQuoteHandling: Optional[str] = None
        mode: Optional[str] = None
        columnNameOfCorruptRecord: Optional[str] = None
        multiLine: Optional[bool] = None
        escapeQuotes: Optional[bool] = None
        quoteAll: Optional[bool] = None
        compression: Optional[str] = None
        partitionColumns: Optional[List[str]] = None
        writeMode: Optional[str] = "error"
        locale: Optional[str] = None
        lineSep: Optional[str] = None
        pathGlobFilter: Optional[str] = None
        modifiedBefore: Optional[str] = None
        modifiedAfter: Optional[str] = None
        recursiveFileLookup: Optional[bool] = None
        createSingleOutputFile: Optional[bool] = None

    props = CsvProperties(  #skiptraversal
        schema = StructType([
          StructField("CustomerID", IntegerType(), True), StructField("Age", IntegerType(), True), StructField("Gender", IntegerType(), True), StructField("Location", StringType(), True)
      ]), 
        description = "", 
        useSchema = True, 
        path = "dbfs:/FileStore/POC01/Airflow/Cust_Airflow_Output.csv", 
        separator = ",", 
        encoding = None, 
        quote = None, 
        escape = None, 
        charToEscapeQuoteEscaping = None, 
        header = True, 
        ignoreLeadingWhiteSpaceReading = None, 
        ignoreTrailingWhiteSpaceReading = None, 
        ignoreLeadingWhiteSpaceWriting = None, 
        ignoreTrailingWhiteSpaceWriting = None, 
        nullValue = None, 
        emptyValue = None, 
        dateFormat = None, 
        timestampFormat = None, 
        comment = None, 
        enforceSchema = None, 
        inferSchema = None, 
        samplingRatio = None, 
        nanValue = None, 
        positiveInf = None, 
        negativeInf = None, 
        maxColumns = None, 
        maxCharsPerColumn = None, 
        unescapedQuoteHandling = None, 
        mode = None, 
        columnNameOfCorruptRecord = None, 
        multiLine = None, 
        escapeQuotes = None, 
        quoteAll = None, 
        compression = None, 
        partitionColumns = None, 
        writeMode = "append", 
        locale = None, 
        lineSep = None, 
        pathGlobFilter = None, 
        modifiedBefore = None, 
        modifiedAfter = None, 
        recursiveFileLookup = None, 
        createSingleOutputFile = True
    )
    in0 = in0
    writer = in0.write

    if props.header is not None:
        writer = writer.option("header", props.header)

    if props.dateFormat is not None:
        writer = writer.option("dateFormat", props.dateFormat)

    if props.escape is not None:
        writer = writer.option("escape", props.escape)

    if props.emptyValue is not None:
        writer = writer.option("emptyValue", props.emptyValue)

    if props.timestampFormat is not None:
        writer = writer.option("timestampFormat", props.timestampFormat)

    if props.quote is not None:
        writer = writer.option("quote", props.quote)

    if props.separator is not None:
        writer = writer.option("sep", props.separator)

    if props.quoteAll is not None:
        writer = writer.option("quoteAll", props.quoteAll)

    if props.encoding is not None:
        writer = writer.option("encoding", props.encoding)

    if props.charToEscapeQuoteEscaping is not None:
        writer = writer.option("charToEscapeQuoteEscaping", props.charToEscapeQuoteEscaping)

    if props.escapeQuotes is not None:
        writer = writer.option("escapeQuotes", props.escapeQuotes)

    if props.ignoreLeadingWhiteSpaceWriting is not None:
        writer = writer.option("ignoreLeadingWhiteSpace", props.ignoreLeadingWhiteSpaceWriting)

    if props.ignoreTrailingWhiteSpaceWriting is not None:
        writer = writer.option("ignoreTrailingWhiteSpace", props.ignoreTrailingWhiteSpaceWriting)

    if props.nullValue is not None:
        writer = writer.option("nullValue", props.nullValue)

    if props.compression is not None:
        writer = writer.option("compression", props.compression)

    if props.lineSep is not None:
        writer = writer.option("lineSep", props.lineSep)

    if props.writeMode is not None:
        writer = writer.mode(props.writeMode)

    if props.partitionColumns is not None and len(props.partitionColumns) > 0:
        writer = writer.partitionBy(*props.partitionColumns)

    writer = writer.option("separator", props.separator).option("header", props.header)

    if props.createSingleOutputFile is not None:
        writer.csv(props.path + "_temp")
    else:
        writer.csv(props.path)

    if props.createSingleOutputFile is not None:
        if props.createSingleOutputFile:
            from prophecy.utils.gems_utils import concatenateFiles
            concatenateFiles(spark, ".csv", props.writeMode, props.path + "_temp", props.path, True, True)
