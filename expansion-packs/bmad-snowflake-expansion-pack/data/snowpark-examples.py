# Snowpark example (illustrative)
from snowflake.snowpark import Session, functions as F
def build_features(session: Session):
    df = session.table("SILVER.ORDERS")
    feats = df.group_by("USER_ID").agg(F.sum("AMOUNT").alias("spend"))
    feats.write.mode("overwrite").save_as_table("FEATURES.USER_SPEND")
