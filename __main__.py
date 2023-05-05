"""An AWS Python Pulumi program"""

import pulumi
from pulumi import export
import pulumi_aws as s3

# Create an AWS resource (S3 Bucket)
bucket = s3.s3.Bucket('my-bucket')


# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)





