import os
file="/home/jkumar/Documents/terraform-oci-design-patterns.tar.gz"
print(os.path.exists(file))
print(os.path.isabs(file))
print(os.path.isdir(file))
print(os.path.isfile(file))
print(os.path.islink(file))
