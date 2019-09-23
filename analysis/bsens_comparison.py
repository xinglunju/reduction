import glob
import os
from astropy.io import fits
from astropy.stats import mad_std

print("{4:14s}{0:>15s} {1:>15s} {2:>15s} {3:>15s} {5:>15s} {6:>15s}".format("bsens_sum", "bsens_mad",  "clean_sum",  "clean_mad", "field & band", "diff_sum", "diff_mad"))

for fn in glob.glob("*bsens_12M_bsens_reclean_robust0.image.tt0.fits"):
    bsens = fn
    clean = fn.replace("_bsens","")
    #print(os.path.exists(bsens), os.path.exists(clean))
    field = fn.split("_uid")[0]

    bsens_fh = fits.open(bsens)
    clean_fh = fits.open(clean)

    if (bsens_fh[0].data.shape == clean_fh[0].data.shape):
        bsd = bsens_fh[0].data
        cld = clean_fh[0].data
        diff = bsd-cld
        bsens_fh[0].data = diff
        bsens_fh.writeto(fn.replace("_bsens_reclean", "_bsens_minus_clean_reclean"), overwrite=False)
        print(f"{field:14s}"
              f"{bsd[np.isfinite(bsd)].sum():15.3f} {mad_std(bsd, ignore_nan=True):15.5f} "
              f"{cld[np.isfinite(cld)].sum():15.3f} {mad_std(cld, ignore_nan=True):15.5f} "
              f"{diff[np.isfinite(diff)].sum():15.3f} {mad_std(diff, ignore_nan=True):15.5f} "
             )
    else:
        print(f"Skipping {bsens} because there was a shape mismatch.")