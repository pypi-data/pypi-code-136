"""lkcom - a Python library of useful routines.

This module contains routines for image processing.

Copyright 2015-2022 Lukas Kontenis
Contact: dse.ssd@gmail.com
"""
import copy
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.image import imsave

from PIL import Image, ImageDraw, ImageFont
import imageio

from lkcom.util import hist_bin_edges_to_centers, handle_general_exception, \
    get_colourmap, isarray

def _crop_base(Iin, R=None, C=None):
    """Crop an imge to the given row and column range."""
    if R is None or C is None:
        return Iin

    # TODO: check R and C ranges agains Iin size

    # crop
    Iout = Iin[R[0]:R[1], C[0]:C[1]]

    return Iout


def crop_rem_rrcc(Iin, U=5, D=5, L=5, R=5):
    """
    *** Internal function to be called from the crop() wrapper ***

    crop an image by removing U and D rows from the top and the bottom, and L
    and R columns from the left and the right.

    Default values: U = D = L = R = 5

    TODO: Update the Matlab version of this
    """

    # Image size
    numR, numC = Iin.shape
    cropR = [U, numR - D]
    cropC = [L, numC - R]

    # crop
    Iout = _crop_base(Iin, cropR, cropC)

    return Iout


def crop_rem_rc(Iin, R=5, C=5):
    """
    *** Internal function to be called from the crop() wrapper ***

    crop an image by removing R rows from the top and the bottom, and C columns
    from the left and the right.

    Default values: R = 5, C = 5

    TODO: Update the Matlab version of this
    """

    # Image size
    numR, numC = Iin.shape
    cropR = [R, numR - R]
    cropC = [C, numC - C]

    # crop
    Iout = _crop_base(Iin, cropR, cropC)

    return Iout


def crop(Iin, R, C):
    """
    crop an image.

    Currently only the two-argument remRC version is supported.
    """

    # TODO: Make sure Iin is valid
    # if(isempty(Iin))
    # Iout = [];
    # return;
    # end

    # TODO:Handle multi-channel images as cell arrays
    # if(iscell(Iin))
    # for ind1 = 1 : size(Iin, 1)
    #    for ind2 = 1 : size(Iin, 2)
    #        Iout{ ind1, ind2 } = dse_Crop(Iin{ ind1, ind2 }, varargin{:});
    #    end
    # end
    # return;
    # end

    # TODO: Handle multi-channel images as 4D arrays
    # if(length(size(Iin)) == 4)
    # for indCh0 = 1 : size(Iin, 3)
    #    for indCh1 = 1 : size(Iin, 4)
    #        Iout(:, :, indCh0, indCh1) = dse_Crop(
    #           Iin(:, :, indCh0, indCh1), varargin{:});
    #    end
    # end
    # return
    # end

    # crop
    Iout = crop_rem_rc(Iin, R, C)

    return Iout


def get_hist_sat_rng(img, frac=0.99, crop_fac=5):
    """
    Get the value range of the image that saturates a given fraction of the
    histogram pixel values. Outlier points are removed before the range is
    calculated.
    """

    # TODO:
    # # == Multi-channel image handling ==
    # if(length(size(img)) > 2)
    # if(length(size(img)) > 4)
    #   dse_PrintWarning(dseWarningEnum.dataformat, [],
    #       'Only images up to 4D are supported');
    #   rng = [0 1];
    #   return;
    # end

    # for ind1 = 1 : size(img, 3)
    #    for ind2 = 1 : size(img, 4)
    #        rng_arr(:, ind1, ind2) = dseIP_ScaleByHist(
    #           img(:, :, ind1, ind2), varargin{:});
    #    end
    # end

    # rng = [min(rng_arr(1,:)), max(rng_arr(2, :))];

    # return;
    # end

    # == Single-channel image handling ==

    # Remove borders where there's a high chance of artefacts
    try:
        if crop_fac != 0:
            img = crop(img, crop_fac, crop_fac)

        # Check if the image contains only NaN values
        if np.isnan(img).any():
            print("Image is only NaN!")
            return [0, 1]

        # Check if the image contains only zero-valued pixels after cropping
        if img[np.isnan(img)] == 0:
            print("Image is empty after cropping")
            return [0, 1]

        # Replace Inf with NaN which still work with histogram ranging. Inf
        # does not
        mask = np.isinf(img)
        if img[mask] == np.nan:
            img[mask] = np.nan
        else:
            img[mask] = 0

        # Calculate initial histogram
        n, binE = np.histogram(img, bins=512)
        binC = hist_bin_edges_to_centers(binE)

        # Identify outlier points by calculating distances between bins having
        # nonzero counts. Bins that are isolated likely contain outlier points.
        # TODO: this assumes zero background, modify to handle images with a
        # background
        binC_nz = binC[n != 0]

        if(binC_nz.size == 1):
            return[binC_nz[0]*0.99, binC_nz[0]*1.01]

        n_nz = n[n != 0]
        binC_nz_d = np.diff(binC_nz)

        # Drop first sample to match binC_nz_d range
        binC_nz = binC_nz[1:]
        n_nz = n_nz[1:]

        # Calculate mean bin distance. For an image with a balanced histogram
        # the mean should be equal to the bin spacing.
        m = np.mean(binC_nz_d)

        # Calculate bin distance std. dev. It should be zero for an image with
        # no outlier points.
        s = np.std(binC_nz_d)

        # Drop bins that are more than three sigmas away from the mean
        mask = np.ones(len(binC_nz_d), dtype=bool)
        mask[binC_nz_d > m + 3*s] = False
        binC_nz = binC_nz[mask]
        n_nz = n_nz[mask]

        # Reduce the histogram range to include a fraction frac of the image
        # pixels
        numpx = sum(n_nz)
        fracpx = frac*numpx

        # Sum over bins until the sum is larger than fracpx
        n_sum = 0
        for ind in range(len(n_nz)):
            n_sum = n_sum + n_nz[ind]
            if s >= fracpx:
                # Return the requested range
                return [binC_nz[0], binC_nz[ind]]

        # Frac is set too high return the full range
        return [binC_nz[0], binC_nz[-1]]
    except Exception:
        handle_general_exception("Could not determine sat range, "
                                 "returning min/max")
        return [img.min(), img.max()]


def get_frac_sat_rng(img, vmin=None, vstep=None, frac=0.999):
    """
    Get a range of values so that 1-frac are saturated.
    """

    if vmin is None:
        vmin = img.min()

    num_act_px = (img >= vmin).sum()

    if vstep is None:
        if img.dtype == np.uint32 or img.dtype == np.uint16 \
                or img.dtype == np.uint8:
            vstep = 1
        else:
            vstep = 1/255

    vmax = vmin

    while((img >= vmax).sum() > num_act_px*(1-frac)):
        vmax = vmax + vstep

    return [vmin, vmax]


def remap_img(img, rng=None, gamma=1, algorithm='FracSat', cap=True):
    """Remap pixel values to the given range and using the given gamma.

    Usage:
        remap_img(img) - remap image using 'HistSat'
        remap_img(img, algorithm='FullRange') - remap image using 'FullRange'
        remap_img(img, rng=range) - remap image to given range
    """

    if rng is None:
        if algorithm == 'HistSat':
            rng = get_hist_sat_rng(img)
        elif algorithm == 'FullRange':
            rng = [img.min(), img.max()]
        elif algorithm == 'FracSat':
            rng = get_frac_sat_rng(img)
        else:
            print("Undefined scaling algorithm " + algorithm)
            return None

    img[img < rng[0]] = rng[0]
    img = img-rng[0]
    if(cap):
        img[img < 0] = 0
    img = img/(rng[1]-rng[0])*255

    if(cap):
        img[img > 255] = 255

    if gamma != 1:
        max_val = img.max()
        img = img/max_val
        img = img**gamma
        # TODO: not sure if using skimage.exposure would be better
        # img = exposure.adjust_gamma(img, gamma)
        img = img*max_val

    return [img, rng]


def normalize(img, min_around_border=False, clip=True):
    """Normalize an image.

    Recalculate image values usnig a linear mapping so that the minimum and
    maximum values correspond to some target values. Typically the minimum and
    maximum correspond to 0.0 and 1.0 so that routines that take floating point
    images display the image correctly.

    If the input data is uint8, the output data is also uint8 with values going
    from 0 to 255. Note that in this case the operation is lossy.

    The source minimum and maximum values are taken as the as min(img) and
    max(img) unless min_around_border is true in which case the minimum value
    is calculated around a border of the image that is 5% of the image size.
    This is useful when the image contains a spurious dark point or severe salt
    and pepper noise which throws off the output image mapping.

    If clip is true values outside the min/max range are clipped at min/max.
    """
    if min_around_border:
        img2 = np.copy(img)
        numr, numc = img2.shape
        from_r = int(numr*0.05)
        to_r = int(numr*0.95)
        from_c = int(numc*0.05)
        to_c = int(numc*0.95)
        img2[from_r:to_r, from_c:to_c] = np.nan
        min_val = np.nanmean(img2)
    else:
        min_val = img.min()

    max_val = img.max()
    dtype = img.dtype

    img = (img - min_val) / (max_val - min_val)

    if clip:
        img[img<0] = 0
        img[img>1] = 1

    if dtype == np.uint8:
        img = np.round(img * 255).astype(np.uint8)

    return img


def bake_cmap(
        img, cmap='magma', rng=None, remap=True,  alpha=None,
        cm_over_val=None, cm_under_val=None):
    """Get an RGB image using a single-channel input and a colourmap."""

    if remap:
        if not rng:
            rng = get_hist_sat_rng(img)

        img = Normalize(rng[0], rng[1], clip=True)(img)

    img_rgb = np.ndarray([img.shape[0], img.shape[1], 3], dtype='uint8')

    cm = copy.copy(get_colourmap(cmap))

    if cm_over_val:
        cm.set_over(cm_over_val)

    if cm_under_val:
        cm.set_under(cm_under_val)

    img_rgb = cm(img)

    if alpha:
        img_rgb[..., -1] = alpha

    return img_rgb

def show_img(img, valrng=None, gamma=1, cmap='magma', remap=True, title=None):
    """
    Show the image on the current axes. By default image pixel values are
    remapped for optimum display dynamic range. To disable this function set
    remap=0. A custom mapping range can be set using valrng=range.
    """

    if remap is True:
        img = remap_img(img, valrng, gamma)
        img = img[0]

    n = mpc.NoNorm
    n.clip = False

    plt.imshow(img, cmap=cmap, norm=n())

    plt.axis("off")
    ax = plt.gca()
    if title:
        ax.set_title(title)

    return ax

def add_scale_bar(img, barL_um=None, pxsz=1):
    """
    Add a scale bare to an RGB image.
    """

    numR, numC, numCh = img.shape

    if not pxsz:
        print("Cannot add scale bar")
        return [img, barL_um]

    if barL_um is None:
        # Determine physical image width
        imgW = numC*pxsz

        # Human-readable scale bar sizes
        L = [200, 100, 50, 20, 10, 5, 2, 1]

        # Find the closest scale bar size that is about 15% of the image
        barL_um = min(L, key=lambda x: abs(x-imgW*0.15))

    barL_px = barL_um/pxsz
    barH_px = barL_px/20

    R = [int(numR - 2*barH_px), int(numR - barH_px)]
    C = [int(numC - barL_px - barH_px), int(numC - barH_px)]
    img[R[0]:R[1], C[0]:C[1], :] = 1

    return [img, barL_um]

def gen_preview_img(Data, cmap='magma'):
    """Generate an image that a human can look at."""
    return bake_cmap(Data, cmap=cmap)


def gen_png(FileName):
    """Generate a PNG file from a text file."""
    img = np.loadtxt(FileName)
    rng = get_hist_sat_rng(img)
    min_val = rng[0]
    img = img-min_val
    img[img < 0] = 0
    max_val = rng[-1]
    img = img/max_val*255
    img[img > 255] = 255
    imsave(FileName[:FileName.rfind('.')] + '.png', img, cmap='magma')


def save_img(img, ImageName="image", img_type="png", suffix='',
             bake_cmap=False, cmap="viridis"):

    if isarray(cmap):
        cmaps = cmap

        for cmap in cmaps:
            save_img(img, ImageName=ImageName, img_type=img_type,
                     suffix=cmap,
                     bake_cmap=bake_cmap, cmap=cmap)

        return

    if(bake_cmap):
        print("Baking colourmap '%s'..." % cmap)
        img = bake_cmap(img/255, cmap=cmap, remap=False,
                        cm_over_val='r', cm_under_val='b')

    if(suffix != ''):
        suffix = '_' + suffix

    FileName = ImageName + suffix + "." + img_type

    print("Saving image '%s'..." % FileName)
    imsave(FileName, img, cmap="gray")


def make_gif(
        images=None, file_names=None, labels=None, output_name='out.gif',
        resize=False, target_sz=None, verbose=False, crop=None, fps=10):
    """Make an animated GIF."""

    # TODO: Test whether imagio version is >=2.6.1

    if images is None and file_names is None:
        print("No images or files given")

    if verbose:
        print("Making GIF at {:.1f} fps...".format(fps))

    if resize:
        if target_sz is None:
            target_w = 600
            target_h = 600
        else:
            target_w = target_sz[0]
            target_h = target_sz[1]

    if file_names is not None:
        if verbose:
            print("Loading {:d} files...".format(len(file_names)))

        images = []
        for ind, file_name in enumerate(file_names):
            images.append(Image.open(file_name))

    frames = []
    for ind, image in enumerate(images):
        if verbose:
            print("Processing frame {:d}/{:d}".format(ind+1, len(images)))
        if crop:
            image = image.crop((crop[0], crop[1], crop[2], crop[3]))
        if(resize):
            src_w, src_h = image.size
            src_ar = src_w/src_h

            if(target_w/src_w > target_h/src_h):
                dst_h = target_h
                dst_w = int(dst_h * src_ar)
            else:
                dst_w = target_w
                dst_h = int(dst_w / src_ar)

            frame = image.resize((dst_w, dst_h), resample=Image.LANCZOS)
        else:
            frame = image
        if labels is not None:
            draw = ImageDraw.Draw(frame)
            font = ImageFont.truetype('arial.ttf', size=45)
            z_str = labels[ind]
            color = 'rgb(255,255,255)'
            draw.text((10, 10), z_str, fill=color, font=font)
        frames.append(frame)

    if(verbose):
        print("Saving GIF")

    # TODO: mimsave might fail if the input PNG files have different sizes
    imageio.mimsave(output_name, frames, format='GIF', fps=fps)
