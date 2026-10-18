from setuptools import find_packages, setup

package_name = 'pubsubdemo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nolan',
    maintainer_email='nolan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "demo_pub = pubsubdemo.publisher:main",
            "demo_sub = pubsubdemo.subscriber:main",
            "demo_srv = pubsubdemo.msgservice:main",
            "demo_client = pubsubdemo.msgclient:main"
        ],
    },
)
