from libcloud.compute.providers import get_driver
from libcloud.compute.types import Provider

#
# This example is wrong and does not use Config()
#
# IT SETS A VERY DANGEROUS EXAMPLE OF HOW NOT TO DOD IT.
#


ACCESS_ID = 'your access id'
SECRET_KEY = 'your secret key'
IMAGE_ID = 'ami-c8052d8d'
SIZE_ID = 't1.micro'

cls = get_driver(Provider.EC2)
driver = cls(ACCESS_ID, SECRET_KEY, region="us-west-1")

sizes = driver.list_sizes()
images = driver.list_images()

size = [s for s in sizes if s.id == SIZE_ID][0]
image = [i for i in images if i.id == IMAGE_ID][0]

node = driver.create_node(name='test-node', image=image, size=size)

elastic_ip = driver.ex_allocate_address()
driver.ex_associate_address_with_node(node, elastic_ip)

driver.ex_disassociate_address(elastic_ip)
driver.ex_release_address(elastic_ip)
