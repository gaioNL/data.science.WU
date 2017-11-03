/*
a
σdocid=10398_txt_earn(frequency)
--->138*/
select count(*)
from frequency
where docid = '10398_txt_earn'
 
/*
b
πterm(σdocid=10398_txt_earn and count=1(frequency))
--->110*/
select count(*)
from frequency
where docid = '10398_txt_earn'
and count = 1
 
 
/*
c
πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))
--->324*/
 
select count(*)
from
(
select term
from frequency
where docid = '10398_txt_earn'
and count = 1
UNION
select term
from frequency
where docid = '925_txt_trade'
and count = 1
)
 
/*
d
count the number of unique documents containing the word "law" or containing the word "legal"
(If a document contains both law and legal, it should only be counted once)
--->58*/
select count(*) from(
select distinct docid
from frequency
where lower(term) = 'law'
or lower(term) = 'legal'
)
 
/*
e
find all documents that have more than 300 total terms, including duplicate terms.
--->107*/
select count(docid)
from(
select docid, sum(count) as term_count
from frequency
group by docid
)
where term_count>300

/*
f
count the number of unique documents that contain both the word 'transactions' and the word 'world'.
--->3*/
 
select count(*) from(
select docid from(
select *
from frequency
where lower(term) = 'transactions'
)
INTERSECT
select docid from(
select *
from frequency
where lower(term) = 'world'
)
)

/*g
Express A X B as a SQL query
--->2874
*/
select val
from(
select a.row_num,b.col_num, sum(a.value * b.value) as val
from a,b
where a.col_num = b.row_num
group by a.row_num,b.col_num
)where row_num = 2 and col_num =3;

/*h
similarity matrix: Write a query to compute the similarity matrix DDT. 
--->19*/
select similarity
from (
	select A.docid as firstDoc, B.docid as secondDoc, sum(A.count*B.count) as similarity
	from frequency as A, frequency as B
	where A.term=B.term
	group by A.docid, B.docid
)
where firstDoc = '10080_txt_crude' and secondDoc = '17035_txt_earn'

/*i
keyword search: Find the best matching document to the keyword query "washington taxes treasury". 
--->6*/
select similarity
from (
     select B.docid as secondDoc, sum(A.count*B.count) as similarity
     from 
        (select *
        from frequency
        union select 'q' as docid, 'washington' as term, 1 as count 
        union select 'q' as docid, 'taxes' as term, 1 as count
        union select 'q' as docid, 'treasury' as term, 1 as count) as A,
        (SELECT *
        FROM frequency
        union select 'q' as docid, 'washington' as term, 1 as count 
        union select 'q' as docid, 'taxes' as term, 1 as count
        union select 'q' as docid, 'treasury' as term, 1 as count) as B
     where A.term=B.term and A.docid='q'
     group by B.docid
)
order by -similarity
limit 1