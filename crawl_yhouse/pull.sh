#!/usr/bin/env bash

echo "=======wx09======="
ssh wx09 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx01======="
ssh wx01 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx02======="
ssh wx02 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx03======="
ssh wx03 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx04======="
ssh wx04 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx05======="
ssh wx05 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx06======="
ssh wx06 "cd /opt/crawl_yhouse/ ; git pull"

echo "=======wx08======="
ssh wx08 "cd /opt/crawl_yhouse/ ; git pull"


