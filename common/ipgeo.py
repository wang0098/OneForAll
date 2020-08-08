import zipfile
import IP2Location
from config.setting import data_storage_dir


zip_path = data_storage_dir.joinpath("IP2LOCATION-LITE-DB3.BIN.ZIP")
bin_path = data_storage_dir.joinpath("IP2LOCATION-LITE-DB3.BIN")
if not bin_path.exists():
    zf = zipfile.ZipFile(zip_path)
    zf.extract('IP2LOCATION-LITE-DB3.BIN', data_storage_dir)
IpGeoInfo = IP2Location.IP2Location(bin_path)
