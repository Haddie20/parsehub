from parsehub.parsers.csv_parser import CSVParser

from parsehub.validators.basic_validator import BasicValidator

from parsehub.reporters.html_reporter import HTMLReporter

from parsehub.pipeline import DataPipeline


raw_data = """
John,25
Jane,30
Mike,40
"""


pipeline = DataPipeline(
    parser=CSVParser(),
    validator=BasicValidator(),
    reporter=HTMLReporter()
)


records = pipeline.process(
    raw_data
)

report = pipeline.report(
    records
)

print(report)