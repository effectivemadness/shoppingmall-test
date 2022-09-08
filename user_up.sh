#!/bin/sh
curl -w " - status code: %{http_code}" k8s-shopping-useringr-9e9aee6926-766594927.ap-northeast-2.elb.amazonaws.com/healthcheck
echo ""
curl -w " - status code: %{http_code}" k8s-shopping-useringr-9e9aee6926-766594927.ap-northeast-2.elb.amazonaws.com/healthcheck/ok
echo ""
curl -w " - status code: %{http_code}" k8s-shopping-useringr-9e9aee6926-766594927.ap-northeast-2.elb.amazonaws.com/healthcheck
echo ""
