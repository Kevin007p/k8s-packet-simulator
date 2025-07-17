#!/bin/bash

for i in {1..500}
do
  curl -s -X POST http://localhost:30007/packet \
    -H "Content-Type: application/json" \
    -d "{\"id\": $i, \"payload\": \"5g data example\"}" &
  sleep 0.05
done
wait
echo "Sent 500 packets."
