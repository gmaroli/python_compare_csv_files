import pandas as pd
import logging
from datetime import datetime
import sys
import os


def dataframe_diff(df1, df2, which=None):
    """
    Find rows which are different
    :param df1: Source DataFrame
    :param df2: Destination DataFrame
    :param which:   Default value in None
                    both        ->   will list records that exist in source and destination (df1 and df2),
                    left_only   ->   will list records that exist only in source (df1),
                    right_only  ->   will list records that exist only in destination(df2)
    :return: dataframe which has output of value based on which param
    """
    comparison_df = df1.merge(df2, indicator=True, how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]

    if which == 'left_only':
        diff_filename = 'diff_sourceonly_{:%Y-%m-%d}.csv'.format(datetime.now())
    elif which == 'right_only':
        diff_filename = 'diff_destonly_{:%Y-%m-%d}.csv'.format(datetime.now())
    else:
        diff_filename = 'diff_both_{:%Y-%m-%d}.csv'.format(datetime.now())

    diff_df.to_csv(diff_filename, index=False)
    logger.info("Result file is stored in the following location: {}".format(os.path.abspath(diff_filename)))
    # return diff_df


def drop_cols(colums_to_drop, coldropdf, reference_file):
    """
    Drops the list of columns from the Dataframe
    :param reference_file: File from where the datafrmae is created
    :param colums_to_drop: Single or comma separated values of the column that are to be dropped
    :param coldropdf: dataframe from which the columns will be dropped
    :return: dataframe after the columns are dropped
    """
    if ',' in colums_to_drop:
        logger.info("Dropping multiple columns: {} in {} ".format(colums_to_drop, reference_file))
        cols = colums_to_drop.split(',')
        for c in cols:
            coldropdf = coldropdf.drop([c.strip()], axis=1)
    else:
        logger.info("Dropping single column: {} in {} ".format(colums_to_drop, reference_file))
        coldropdf = coldropdf.drop([colums_to_drop.strip()], axis=1)
    return coldropdf


if __name__ == '__main__':
    try:
        LOG_FILE_NAME = 'CompareCsv_{:%Y-%m-%d}.log'.format(datetime.now())
        logger = logging.getLogger("Compare two csv files")
        logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler('{0}'.format(LOG_FILE_NAME), 'a')
        fh.setLevel(logging.DEBUG)

        formatterfh = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatterfh)
        logger.addHandler(fh)
        logger.info("{0}{1}{2}".format("*" * 50, "START", "*" * 50))

        # create console handler with a higher log level
        formatterch = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatterch)
        logger.addHandler(ch)

        logger.info("Log files will be written to: {0}".format(os.path.abspath(LOG_FILE_NAME)))

        sourcefile = input("Enter the source file path:")
        logger.info("Source File Path: {}".format(sourcefile))
        destfile = input("Enter the destination file path: ")
        logger.info("Destination File Path: {}".format(destfile))

        sourcedf = pd.read_csv(sourcefile)
        destdf = pd.read_csv(destfile)

        sourcecols2drop = input("Columns to be dropped in the source file (comma separted values if more than one column). Press <Enter> to skip: ")
        destcols2drop = input("Columns to be dropped in the destination file (comma separted values if more than one column). Press <Enter> to skip: ")

        if sourcecols2drop:
            sourcedf = drop_cols(sourcecols2drop, sourcedf, sourcefile)
        if destcols2drop:
            destdf = drop_cols(destcols2drop, destdf, destfile)

        # compareType = input("Enter value for match type (source_only, dest_only or both): ")
        match_dict = {'source_only': 'left_only', 'dest_only': 'right_only', 'both': 'both'}

        for compareType in match_dict:
            dataframe_diff(sourcedf, destdf, match_dict[compareType])
        # logger.info("Match type: {}".format(compareType))
        # if compareType in match_dict.keys():

        logger.info("{0}{1}{2}".format("*" * 50, "END", "*" * 50))
        exit_cmd = input("Press enter to exit")

    except Exception as e:
        logger.error("Error Occured: {0}".format(sys.exc_info()))
        logger.info("{0}{1}{2}".format("*" * 50, "END", "*" * 50))
        exit_cmd = input("Press enter to exit")
