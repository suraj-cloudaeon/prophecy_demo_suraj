from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_airflow_test.config.ConfigStore import *
from pl_airflow_test.udfs.UDFs import *

def ds_airflow_src(spark: SparkSession) -> DataFrame:
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
          StructField("CustomerID", StringType(), True), StructField("Age", StringType(), True), StructField("Gender", StringType(), True), StructField("Location", StringType(), True)
      ]), 
        description = "", 
        useSchema = True, 
        path = "dbfs:/FileStore/POC01/Customer_Data.txt", 
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
        writeMode = "error", 
        locale = None, 
        lineSep = None, 
        pathGlobFilter = None, 
        modifiedBefore = None, 
        modifiedAfter = None, 
        recursiveFileLookup = None, 
        createSingleOutputFile = None
    )
    reader = spark.read

    if props.schema is not None and props.useSchema:
        reader = reader.schema(props.schema)

    if props.negativeInf is not None:
        reader = reader.option("negativeInf", props.negativeInf)

    if props.maxCharsPerColumn is not None:
        reader = reader.option("maxCharsPerColumn", props.maxCharsPerColumn)

    if props.header is not None:
        reader = reader.option("header", props.header)

    if props.inferSchema is not None:
        reader = reader.option("inferSchema", props.inferSchema)

    if props.mode is not None:
        reader = reader.option("mode", props.mode)

    if props.dateFormat is not None:
        reader = reader.option("dateFormat", props.dateFormat)

    if props.samplingRatio is not None:
        reader = reader.option("samplingRatio", props.samplingRatio.value)

    if props.positiveInf is not None:
        reader = reader.option("positiveInf", props.positiveInf)

    if props.escape is not None:
        reader = reader.option("escape", props.escape)

    if props.emptyValue is not None:
        reader = reader.option("emptyValue", props.emptyValue)

    if props.timestampFormat is not None:
        reader = reader.option("timestampFormat", props.timestampFormat)

    if props.quote is not None:
        reader = reader.option("quote", props.quote)

    if props.separator is not None:
        reader = reader.option("sep", props.separator)

    if props.enforceSchema is not None:
        reader = reader.option("enforceSchema", props.enforceSchema)

    if props.encoding is not None:
        reader = reader.option("encoding", props.encoding)

    if props.comment is not None:
        reader = reader.option("comment", props.comment)

    if props.locale is not None:
        reader = reader.option("locale", props.locale)

    if props.lineSep is not None:
        reader = reader.option("lineSep", props.lineSep)

    if props.unescapedQuoteHandling is not None:
        reader = reader.option("unescapedQuoteHandling", props.unescapedQuoteHandling)

    if props.charToEscapeQuoteEscaping is not None:
        reader = reader.option("charToEscapeQuoteEscaping", props.charToEscapeQuoteEscaping)

    if props.nanValue is not None:
        reader = reader.option("nanValue", props.nanValue)

    if props.ignoreLeadingWhiteSpaceWriting is not None:
        reader = reader.option("ignoreLeadingWhiteSpace", props.ignoreLeadingWhiteSpaceWriting)

    if props.ignoreTrailingWhiteSpaceWriting is not None:
        reader = reader.option("ignoreTrailingWhiteSpace", props.ignoreTrailingWhiteSpaceWriting)

    if props.nullValue is not None:
        reader = reader.option("nullValue", props.nullValue)

    if props.maxColumns is not None:
        reader = reader.option("maxColumns", props.maxColumns)

    if props.multiLine is not None:
        reader = reader.option("multiLine", props.multiLine)

    if props.modifiedBefore is not None:
        reader = reader.option("modifiedBefore", props.modifiedBefore)

    if props.modifiedAfter is not None:
        reader = reader.option("modifiedAfter", props.modifiedAfter)

    if props.recursiveFileLookup is not None:
        reader = reader.option("recursiveFileLookup", props.recursiveFileLookup)

    if props.pathGlobFilter is not None:
        reader = reader.option("pathGlobFilter", props.pathGlobFilter)

    if props.columnNameOfCorruptRecord is not None:
        reader = reader.option("columnNameOfCorruptRecord", props.columnNameOfCorruptRecord)

    return reader.csv(props.path)
