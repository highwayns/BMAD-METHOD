-- Network policy examples
CREATE NETWORK POLICY corp_policy ALLOWED_IP_LIST=('203.0.113.0/24') BLOCKED_IP_LIST=('0.0.0.0/0');
ALTER ACCOUNT SET NETWORK_POLICY = corp_policy;
