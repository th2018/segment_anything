from samgeo import SamGeo, show_image, download_file, overlay_images, tms_to_geotiff
image = "orthomosaic.tif"
sam = SamGeo(model_type="vit_h")
sam.generate(image, output="masks.tif")
