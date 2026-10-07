provider "aws" {
  region = "us-east-1"
}

resource "aws_ebs_volume" "test_wasted_volume" {
  availability_zone = "us-east-1a"
  size              = 10

  tags = {
    Name = "CloudJanitorTestVolume"
  }
}