provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = "eu-west-2"
}
resource "aws_instance" "instance" {
  ami           = var.ami
  instance_type = var.vm_type
  key_name      = "host1"
}
resource "aws_s3_bucket" "my_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
