#!/bin/bash
to=10
cont=$(docker run --rm -d -v `pwd`/temp/$1:/compile compiler:v1 /bin/bash -c "$2" )

code=$(timeout "$to" docker wait "$cont" || true)
docker kill $cont &> /dev/null
echo -n 'status: '
if [ -z "$code" ]; then
    echo timeout
else
    echo exited: $code
fi

#echo output:
# pipe to sed simply for pretty nice indentation
#docker logs $cont | sed 's/^/\t/'

#docker rm $cont &> /dev/null
