#!/usr/bin/python3
#coding=utf-8

# python3 cli_click.py get-weekday --date 2013-05-31
# python3 cli_click.py dots --n=12
# python3 cli_click.py dots --n 12
# python3 cli_click.py findme --pos 2 3
# python3 cli_click.py putitem --item dec 1
import click
import datetime


@click.group()
def cli():
    pass

@click.command()
@click.option('--date', default='now',help='the date format "yyyy-mm-dd"')
def get_weekday(date):
    if date == 'now':
        date = datetime.datetime.utcnow()
    else:
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
    click.echo(date.strftime('%A'))

@click.command()
@click.option('--date1', help='the date format "yyyy-mm-dd"')
@click.option('--date2', help='the date format "yyyy-mm-dd"')
def delta_day(date1, date2):
    date1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2,'%Y-%m-%d')
    delta = date1 - date2 if date1 > date2 else date2-date1
    click.echo(delta.days)

@click.command()
@click.option('--n',default=1)
def dots(n):
    click.echo('.' * n)

@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    click.echo('%s / %s' % pos)

@click.command()
@click.option('--item', type=(str, float))
def putitem(item):
    click.echo('name=%s id=%d' % item)

@click.command()
@click.option('--input', type=click.File('r'))
@click.option('--output', type=click.File('w'))
def inout(input,output):
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)

cli.add_command(get_weekday)
cli.add_command(delta_day)
cli.add_command(dots)
cli.add_command(findme)
cli.add_command(putitem)



if __name__=='__main__':
    cli()