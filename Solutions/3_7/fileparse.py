# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True,delimiter=','):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f,delimiter)

        # 헤더를 읽음
        headers = next(rows) if has_headers else []

        if select:
            indice = [headers.index(x) for x in select]
            headers = select
        records = []
        for row in rows:
            if not row:    # 데이터가 없는 행을 건너뜀
                continue

            if indice:
                row = [row[x] for x in indice]

            if types:
                row = [func(x) for func,x in zip(types,row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records