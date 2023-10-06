# Databricks notebook source
print("hello, World")

# COMMAND ----------

print("Hello data engineering")

# COMMAND ----------

# MAGIC %sql  --magic command
# MAGIC SELECT "HELLO WORLD"
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## title 2
# MAGIC
# MAGIC |user_id|user_name|
# MAGIC |-------|---------|
# MAGIC |   1   |  Adam   |

# COMMAND ----------

# MAGIC %run ./includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

# MAGIC %fs ls '/includes'

# COMMAND ----------

dbutils.help()


# COMMAND ----------

dbutils.fs.help()


# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------

dbutils.fs.vi('databricks-datasets/README.md')

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT"Today I am feeling curious"
# MAGIC

# COMMAND ----------


