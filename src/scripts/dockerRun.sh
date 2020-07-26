#!/bin/bash
to=10
cont=$(docker run -d -v $1:/compile compiler:v1 /bin/bash -c "$2" )
code=$(timeout "$to" docker wait "$cont" || true)
docker kill $cont &> /dev/null
echo -n 'status: '
if [ -z "$code" ]; then
    echo timeout
else
    echo exited: $code
fi
