output "vm_public_ip" {
    value = aws_instance.instance.public_ip
}
output "bucket_domain" {
  value = aws_s3_bucket.my_bucket.bucket_domain_name
}
