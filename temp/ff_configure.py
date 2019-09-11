#!/bin/python3
import os
import shutil
import subprocess

def exist(cmd: str):
    return True if shutil.which(cmd) is not None else True

def exec(cmd: str, *args):
    ca = [cmd]
    ca.extend(*args)
    print(ca)
    subprocess.call(ca)
    # print(cmd)
    # print(*args)

def try_exec(cmd: str, *args):
    print('Trying shell ' + cmd)
    if exist(cmd):
        exec(cmd, args)

def log(*args):
    print(args)
    # echo "$@" >> $logfile

if __name__=='__main__':
    print('''FFmpeg configure script

Copyright (c) 2000-2002 Fabrice Bellard
Copyright (c) 2005-2008 Diego Biurrun
Copyright (c) 2005-2008 Mans Rullgard
''')

# #!/bin/sh
# #
# # FFmpeg configure script
# #
# # Copyright (c) 2000-2002 Fabrice Bellard
# # Copyright (c) 2005-2008 Diego Biurrun
# # Copyright (c) 2005-2008 Mans Rullgard
# #

# # Prevent locale nonsense from breaking basic text processing.
# LC_ALL=C
# export LC_ALL

# # make sure we are running under a compatible shell
# # try to make this part work with most shells

# try_exec(){
#     echo "Trying shell $1"
#     type "$1" > /dev/null 2>&1 && exec "$@"
# }

# unset foo
# (: ${foo%%bar}) 2> /dev/null
# E1="$?"

# (: ${foo?}) 2> /dev/null
# E2="$?"

# if test "$E1" != 0 || test "$E2" = 0; then
#     echo "Broken shell detected.  Trying alternatives."
#     export FF_CONF_EXEC
#     if test "0$FF_CONF_EXEC" -lt 1; then
#         FF_CONF_EXEC=1
#         try_exec bash "$0" "$@"
#     fi
#     if test "0$FF_CONF_EXEC" -lt 2; then
#         FF_CONF_EXEC=2
#         try_exec ksh "$0" "$@"
#     fi
#     if test "0$FF_CONF_EXEC" -lt 3; then
#         FF_CONF_EXEC=3
#         try_exec /usr/xpg4/bin/sh "$0" "$@"
#     fi
#     echo "No compatible shell script interpreter found."
#     echo "This configure script requires a POSIX-compatible shell"
#     echo "such as bash or ksh."
#     echo "THIS IS NOT A BUG IN FFMPEG, DO NOT REPORT IT AS SUCH."
#     echo "Instead, install a working POSIX-compatible shell."
#     echo "Disabling this configure test will create a broken FFmpeg."
#     if test "$BASH_VERSION" = '2.04.0(1)-release'; then
#         echo "This bash version ($BASH_VERSION) is broken on your platform."
#         echo "Upgrade to a later version if available."
#     fi
#     exit 1
# fi

# test -d /usr/xpg4/bin && PATH=/usr/xpg4/bin:$PATH

# show_help(){
#     cat <<EOF
# Usage: configure [options]
# Options: [defaults in brackets after descriptions]

# Help options:
#   --help                   print this message
#   --quiet                  Suppress showing informative output
#   --list-decoders          show all available decoders
#   --list-encoders          show all available encoders
#   --list-hwaccels          show all available hardware accelerators
#   --list-demuxers          show all available demuxers
#   --list-muxers            show all available muxers
#   --list-parsers           show all available parsers
#   --list-protocols         show all available protocols
#   --list-bsfs              show all available bitstream filters
#   --list-indevs            show all available input devices
#   --list-outdevs           show all available output devices
#   --list-filters           show all available filters

# Standard options:
#   --logfile=FILE           log tests and output to FILE [ffbuild/config.log]
#   --disable-logging        do not log configure debug information
#   --fatal-warnings         fail if any configure warning is generated
#   --prefix=PREFIX          install in PREFIX [$prefix_default]
#   --bindir=DIR             install binaries in DIR [PREFIX/bin]
#   --datadir=DIR            install data files in DIR [PREFIX/share/ffmpeg]
#   --docdir=DIR             install documentation in DIR [PREFIX/share/doc/ffmpeg]
#   --libdir=DIR             install libs in DIR [PREFIX/lib]
#   --shlibdir=DIR           install shared libs in DIR [LIBDIR]
#   --incdir=DIR             install includes in DIR [PREFIX/include]
#   --mandir=DIR             install man page in DIR [PREFIX/share/man]
#   --pkgconfigdir=DIR       install pkg-config files in DIR [LIBDIR/pkgconfig]
#   --enable-rpath           use rpath to allow installing libraries in paths
#                            not part of the dynamic linker search path
#                            use rpath when linking programs (USE WITH CARE)
#   --install-name-dir=DIR   Darwin directory name for installed targets

# Licensing options:
#   --enable-gpl             allow use of GPL code, the resulting libs
#                            and binaries will be under GPL [no]
#   --enable-version3        upgrade (L)GPL to version 3 [no]
#   --enable-nonfree         allow use of nonfree code, the resulting libs
#                            and binaries will be unredistributable [no]

# Configuration options:
#   --disable-static         do not build static libraries [no]
#   --enable-shared          build shared libraries [no]
#   --enable-small           optimize for size instead of speed
#   --disable-runtime-cpudetect disable detecting CPU capabilities at runtime (smaller binary)
#   --enable-gray            enable full grayscale support (slower color)
#   --disable-swscale-alpha  disable alpha channel support in swscale
#   --disable-all            disable building components, libraries and programs
#   --disable-autodetect     disable automatically detected external libraries [no]

# Program options:
#   --disable-programs       do not build command line programs
#   --disable-ffmpeg         disable ffmpeg build
#   --disable-ffplay         disable ffplay build
#   --disable-ffprobe        disable ffprobe build

# Documentation options:
#   --disable-doc            do not build documentation
#   --disable-htmlpages      do not build HTML documentation pages
#   --disable-manpages       do not build man documentation pages
#   --disable-podpages       do not build POD documentation pages
#   --disable-txtpages       do not build text documentation pages

# Component options:
#   --disable-avdevice       disable libavdevice build
#   --disable-avcodec        disable libavcodec build
#   --disable-avformat       disable libavformat build
#   --disable-swresample     disable libswresample build
#   --disable-swscale        disable libswscale build
#   --disable-postproc       disable libpostproc build
#   --disable-avfilter       disable libavfilter build
#   --enable-avresample      enable libavresample build (deprecated) [no]
#   --disable-pthreads       disable pthreads [autodetect]
#   --disable-w32threads     disable Win32 threads [autodetect]
#   --disable-os2threads     disable OS/2 threads [autodetect]
#   --disable-network        disable network support [no]
#   --disable-dct            disable DCT code
#   --disable-dwt            disable DWT code
#   --disable-error-resilience disable error resilience code
#   --disable-lsp            disable LSP code
#   --disable-lzo            disable LZO decoder code
#   --disable-mdct           disable MDCT code
#   --disable-rdft           disable RDFT code
#   --disable-fft            disable FFT code
#   --disable-faan           disable floating point AAN (I)DCT code
#   --disable-pixelutils     disable pixel utils in libavutil

# Individual component options:
#   --disable-everything     disable all components listed below
#   --disable-encoder=NAME   disable encoder NAME
#   --enable-encoder=NAME    enable encoder NAME
#   --disable-encoders       disable all encoders
#   --disable-decoder=NAME   disable decoder NAME
#   --enable-decoder=NAME    enable decoder NAME
#   --disable-decoders       disable all decoders
#   --disable-hwaccel=NAME   disable hwaccel NAME
#   --enable-hwaccel=NAME    enable hwaccel NAME
#   --disable-hwaccels       disable all hwaccels
#   --disable-muxer=NAME     disable muxer NAME
#   --enable-muxer=NAME      enable muxer NAME
#   --disable-muxers         disable all muxers
#   --disable-demuxer=NAME   disable demuxer NAME
#   --enable-demuxer=NAME    enable demuxer NAME
#   --disable-demuxers       disable all demuxers
#   --enable-parser=NAME     enable parser NAME
#   --disable-parser=NAME    disable parser NAME
#   --disable-parsers        disable all parsers
#   --enable-bsf=NAME        enable bitstream filter NAME
#   --disable-bsf=NAME       disable bitstream filter NAME
#   --disable-bsfs           disable all bitstream filters
#   --enable-protocol=NAME   enable protocol NAME
#   --disable-protocol=NAME  disable protocol NAME
#   --disable-protocols      disable all protocols
#   --enable-indev=NAME      enable input device NAME
#   --disable-indev=NAME     disable input device NAME
#   --disable-indevs         disable input devices
#   --enable-outdev=NAME     enable output device NAME
#   --disable-outdev=NAME    disable output device NAME
#   --disable-outdevs        disable output devices
#   --disable-devices        disable all devices
#   --enable-filter=NAME     enable filter NAME
#   --disable-filter=NAME    disable filter NAME
#   --disable-filters        disable all filters

# External library support:

#   Using any of the following switches will allow FFmpeg to link to the
#   corresponding external library. All the components depending on that library
#   will become enabled, if all their other dependencies are met and they are not
#   explicitly disabled. E.g. --enable-libwavpack will enable linking to
#   libwavpack and allow the libwavpack encoder to be built, unless it is
#   specifically disabled with --disable-encoder=libwavpack.

#   Note that only the system libraries are auto-detected. All the other external
#   libraries must be explicitly enabled.

#   Also note that the following help text describes the purpose of the libraries
#   themselves, not all their features will necessarily be usable by FFmpeg.

#   --disable-alsa           disable ALSA support [autodetect]
#   --disable-appkit         disable Apple AppKit framework [autodetect]
#   --disable-avfoundation   disable Apple AVFoundation framework [autodetect]
#   --enable-avisynth        enable reading of AviSynth script files [no]
#   --disable-bzlib          disable bzlib [autodetect]
#   --disable-coreimage      disable Apple CoreImage framework [autodetect]
#   --enable-chromaprint     enable audio fingerprinting with chromaprint [no]
#   --enable-frei0r          enable frei0r video filtering [no]
#   --enable-gcrypt          enable gcrypt, needed for rtmp(t)e support
#                            if openssl, librtmp or gmp is not used [no]
#   --enable-gmp             enable gmp, needed for rtmp(t)e support
#                            if openssl or librtmp is not used [no]
#   --enable-gnutls          enable gnutls, needed for https support
#                            if openssl, libtls or mbedtls is not used [no]
#   --disable-iconv          disable iconv [autodetect]
#   --enable-jni             enable JNI support [no]
#   --enable-ladspa          enable LADSPA audio filtering [no]
#   --enable-libaom          enable AV1 video encoding/decoding via libaom [no]
#   --enable-libaribb24      enable ARIB text and caption decoding via libaribb24 [no]
#   --enable-libass          enable libass subtitles rendering,
#                            needed for subtitles and ass filter [no]
#   --enable-libbluray       enable BluRay reading using libbluray [no]
#   --enable-libbs2b         enable bs2b DSP library [no]
#   --enable-libcaca         enable textual display using libcaca [no]
#   --enable-libcelt         enable CELT decoding via libcelt [no]
#   --enable-libcdio         enable audio CD grabbing with libcdio [no]
#   --enable-libcodec2       enable codec2 en/decoding using libcodec2 [no]
#   --enable-libdav1d        enable AV1 decoding via libdav1d [no]
#   --enable-libdavs2        enable AVS2 decoding via libdavs2 [no]
#   --enable-libdc1394       enable IIDC-1394 grabbing using libdc1394
#                            and libraw1394 [no]
#   --enable-libfdk-aac      enable AAC de/encoding via libfdk-aac [no]
#   --enable-libflite        enable flite (voice synthesis) support via libflite [no]
#   --enable-libfontconfig   enable libfontconfig, useful for drawtext filter [no]
#   --enable-libfreetype     enable libfreetype, needed for drawtext filter [no]
#   --enable-libfribidi      enable libfribidi, improves drawtext filter [no]
#   --enable-libgme          enable Game Music Emu via libgme [no]
#   --enable-libgsm          enable GSM de/encoding via libgsm [no]
#   --enable-libiec61883     enable iec61883 via libiec61883 [no]
#   --enable-libilbc         enable iLBC de/encoding via libilbc [no]
#   --enable-libjack         enable JACK audio sound server [no]
#   --enable-libklvanc       enable Kernel Labs VANC processing [no]
#   --enable-libkvazaar      enable HEVC encoding via libkvazaar [no]
#   --enable-liblensfun      enable lensfun lens correction [no]
#   --enable-libmodplug      enable ModPlug via libmodplug [no]
#   --enable-libmp3lame      enable MP3 encoding via libmp3lame [no]
#   --enable-libopencore-amrnb enable AMR-NB de/encoding via libopencore-amrnb [no]
#   --enable-libopencore-amrwb enable AMR-WB decoding via libopencore-amrwb [no]
#   --enable-libopencv       enable video filtering via libopencv [no]
#   --enable-libopenh264     enable H.264 encoding via OpenH264 [no]
#   --enable-libopenjpeg     enable JPEG 2000 de/encoding via OpenJPEG [no]
#   --enable-libopenmpt      enable decoding tracked files via libopenmpt [no]
#   --enable-libopus         enable Opus de/encoding via libopus [no]
#   --enable-libpulse        enable Pulseaudio input via libpulse [no]
#   --enable-librsvg         enable SVG rasterization via librsvg [no]
#   --enable-librubberband   enable rubberband needed for rubberband filter [no]
#   --enable-librtmp         enable RTMP[E] support via librtmp [no]
#   --enable-libshine        enable fixed-point MP3 encoding via libshine [no]
#   --enable-libsmbclient    enable Samba protocol via libsmbclient [no]
#   --enable-libsnappy       enable Snappy compression, needed for hap encoding [no]
#   --enable-libsoxr         enable Include libsoxr resampling [no]
#   --enable-libspeex        enable Speex de/encoding via libspeex [no]
#   --enable-libsrt          enable Haivision SRT protocol via libsrt [no]
#   --enable-libssh          enable SFTP protocol via libssh [no]
#   --enable-libtensorflow   enable TensorFlow as a DNN module backend
#                            for DNN based filters like sr [no]
#   --enable-libtesseract    enable Tesseract, needed for ocr filter [no]
#   --enable-libtheora       enable Theora encoding via libtheora [no]
#   --enable-libtls          enable LibreSSL (via libtls), needed for https support
#                            if openssl, gnutls or mbedtls is not used [no]
#   --enable-libtwolame      enable MP2 encoding via libtwolame [no]
#   --enable-libv4l2         enable libv4l2/v4l-utils [no]
#   --enable-libvidstab      enable video stabilization using vid.stab [no]
#   --enable-libvmaf         enable vmaf filter via libvmaf [no]
#   --enable-libvo-amrwbenc  enable AMR-WB encoding via libvo-amrwbenc [no]
#   --enable-libvorbis       enable Vorbis en/decoding via libvorbis,
#                            native implementation exists [no]
#   --enable-libvpx          enable VP8 and VP9 de/encoding via libvpx [no]
#   --enable-libwavpack      enable wavpack encoding via libwavpack [no]
#   --enable-libwebp         enable WebP encoding via libwebp [no]
#   --enable-libx264         enable H.264 encoding via x264 [no]
#   --enable-libx265         enable HEVC encoding via x265 [no]
#   --enable-libxavs         enable AVS encoding via xavs [no]
#   --enable-libxavs2        enable AVS2 encoding via xavs2 [no]
#   --enable-libxcb          enable X11 grabbing using XCB [autodetect]
#   --enable-libxcb-shm      enable X11 grabbing shm communication [autodetect]
#   --enable-libxcb-xfixes   enable X11 grabbing mouse rendering [autodetect]
#   --enable-libxcb-shape    enable X11 grabbing shape rendering [autodetect]
#   --enable-libxvid         enable Xvid encoding via xvidcore,
#                            native MPEG-4/Xvid encoder exists [no]
#   --enable-libxml2         enable XML parsing using the C library libxml2, needed
#                            for dash demuxing support [no]
#   --enable-libzimg         enable z.lib, needed for zscale filter [no]
#   --enable-libzmq          enable message passing via libzmq [no]
#   --enable-libzvbi         enable teletext support via libzvbi [no]
#   --enable-lv2             enable LV2 audio filtering [no]
#   --disable-lzma           disable lzma [autodetect]
#   --enable-decklink        enable Blackmagic DeckLink I/O support [no]
#   --enable-mbedtls         enable mbedTLS, needed for https support
#                            if openssl, gnutls or libtls is not used [no]
#   --enable-mediacodec      enable Android MediaCodec support [no]
#   --enable-libmysofa       enable libmysofa, needed for sofalizer filter [no]
#   --enable-openal          enable OpenAL 1.1 capture support [no]
#   --enable-opencl          enable OpenCL processing [no]
#   --enable-opengl          enable OpenGL rendering [no]
#   --enable-openssl         enable openssl, needed for https support
#                            if gnutls, libtls or mbedtls is not used [no]
#   --enable-pocketsphinx    enable PocketSphinx, needed for asr filter [no]
#   --disable-sndio          disable sndio support [autodetect]
#   --disable-schannel       disable SChannel SSP, needed for TLS support on
#                            Windows if openssl and gnutls are not used [autodetect]
#   --disable-sdl2           disable sdl2 [autodetect]
#   --disable-securetransport disable Secure Transport, needed for TLS support
#                            on OSX if openssl and gnutls are not used [autodetect]
#   --enable-vapoursynth     enable VapourSynth demuxer [no]
#   --disable-xlib           disable xlib [autodetect]
#   --disable-zlib           disable zlib [autodetect]

#   The following libraries provide various hardware acceleration features:
#   --disable-amf            disable AMF video encoding code [autodetect]
#   --disable-audiotoolbox   disable Apple AudioToolbox code [autodetect]
#   --enable-cuda-nvcc       enable Nvidia CUDA compiler [no]
#   --disable-cuda-llvm      disable CUDA compilation using clang [autodetect]
#   --disable-cuvid          disable Nvidia CUVID support [autodetect]
#   --disable-d3d11va        disable Microsoft Direct3D 11 video acceleration code [autodetect]
#   --disable-dxva2          disable Microsoft DirectX 9 video acceleration code [autodetect]
#   --disable-ffnvcodec      disable dynamically linked Nvidia code [autodetect]
#   --enable-libdrm          enable DRM code (Linux) [no]
#   --enable-libmfx          enable Intel MediaSDK (AKA Quick Sync Video) code via libmfx [no]
#   --enable-libnpp          enable Nvidia Performance Primitives-based code [no]
#   --enable-mmal            enable Broadcom Multi-Media Abstraction Layer (Raspberry Pi) via MMAL [no]
#   --disable-nvdec          disable Nvidia video decoding acceleration (via hwaccel) [autodetect]
#   --disable-nvenc          disable Nvidia video encoding code [autodetect]
#   --enable-omx             enable OpenMAX IL code [no]
#   --enable-omx-rpi         enable OpenMAX IL code for Raspberry Pi [no]
#   --enable-rkmpp           enable Rockchip Media Process Platform code [no]
#   --disable-v4l2-m2m       disable V4L2 mem2mem code [autodetect]
#   --disable-vaapi          disable Video Acceleration API (mainly Unix/Intel) code [autodetect]
#   --disable-vdpau          disable Nvidia Video Decode and Presentation API for Unix code [autodetect]
#   --disable-videotoolbox   disable VideoToolbox code [autodetect]

# Toolchain options:
#   --arch=ARCH              select architecture [$arch]
#   --cpu=CPU                select the minimum required CPU (affects
#                            instruction selection, may crash on older CPUs)
#   --cross-prefix=PREFIX    use PREFIX for compilation tools [$cross_prefix]
#   --progs-suffix=SUFFIX    program name suffix []
#   --enable-cross-compile   assume a cross-compiler is used
#   --sysroot=PATH           root of cross-build tree
#   --sysinclude=PATH        location of cross-build system headers
#   --target-os=OS           compiler targets OS [$target_os]
#   --target-exec=CMD        command to run executables on target
#   --target-path=DIR        path to view of build directory on target
#   --target-samples=DIR     path to samples directory on target
#   --tempprefix=PATH        force fixed dir/prefix instead of mktemp for checks
#   --toolchain=NAME         set tool defaults according to NAME
#                            (gcc-asan, clang-asan, gcc-msan, clang-msan,
#                            gcc-tsan, clang-tsan, gcc-usan, clang-usan,
#                            valgrind-massif, valgrind-memcheck,
#                            msvc, icl, gcov, llvm-cov, hardened)
#   --nm=NM                  use nm tool NM [$nm_default]
#   --ar=AR                  use archive tool AR [$ar_default]
#   --as=AS                  use assembler AS [$as_default]
#   --ln_s=LN_S              use symbolic link tool LN_S [$ln_s_default]
#   --strip=STRIP            use strip tool STRIP [$strip_default]
#   --windres=WINDRES        use windows resource compiler WINDRES [$windres_default]
#   --x86asmexe=EXE          use nasm-compatible assembler EXE [$x86asmexe_default]
#   --cc=CC                  use C compiler CC [$cc_default]
#   --cxx=CXX                use C compiler CXX [$cxx_default]
#   --objcc=OCC              use ObjC compiler OCC [$cc_default]
#   --dep-cc=DEPCC           use dependency generator DEPCC [$cc_default]
#   --nvcc=NVCC              use Nvidia CUDA compiler NVCC or clang [$nvcc_default]
#   --ld=LD                  use linker LD [$ld_default]
#   --pkg-config=PKGCONFIG   use pkg-config tool PKGCONFIG [$pkg_config_default]
#   --pkg-config-flags=FLAGS pass additional flags to pkgconf []
#   --ranlib=RANLIB          use ranlib RANLIB [$ranlib_default]
#   --doxygen=DOXYGEN        use DOXYGEN to generate API doc [$doxygen_default]
#   --host-cc=HOSTCC         use host C compiler HOSTCC
#   --host-cflags=HCFLAGS    use HCFLAGS when compiling for host
#   --host-cppflags=HCPPFLAGS use HCPPFLAGS when compiling for host
#   --host-ld=HOSTLD         use host linker HOSTLD
#   --host-ldflags=HLDFLAGS  use HLDFLAGS when linking for host
#   --host-extralibs=HLIBS   use libs HLIBS when linking for host
#   --host-os=OS             compiler host OS [$target_os]
#   --extra-cflags=ECFLAGS   add ECFLAGS to CFLAGS [$CFLAGS]
#   --extra-cxxflags=ECFLAGS add ECFLAGS to CXXFLAGS [$CXXFLAGS]
#   --extra-objcflags=FLAGS  add FLAGS to OBJCFLAGS [$CFLAGS]
#   --extra-ldflags=ELDFLAGS add ELDFLAGS to LDFLAGS [$LDFLAGS]
#   --extra-ldexeflags=ELDFLAGS add ELDFLAGS to LDEXEFLAGS [$LDEXEFLAGS]
#   --extra-ldsoflags=ELDFLAGS add ELDFLAGS to LDSOFLAGS [$LDSOFLAGS]
#   --extra-libs=ELIBS       add ELIBS [$ELIBS]
#   --extra-version=STRING   version string suffix []
#   --optflags=OPTFLAGS      override optimization-related compiler flags
#   --nvccflags=NVCCFLAGS    override nvcc flags [$nvccflags_default]
#   --build-suffix=SUFFIX    library name suffix []
#   --enable-pic             build position-independent code
#   --enable-thumb           compile for Thumb instruction set
#   --enable-lto             use link-time optimization
#   --env="ENV=override"     override the environment variables

# Advanced options (experts only):
#   --malloc-prefix=PREFIX   prefix malloc and related names with PREFIX
#   --custom-allocator=NAME  use a supported custom allocator
#   --disable-symver         disable symbol versioning
#   --enable-hardcoded-tables use hardcoded tables instead of runtime generation
#   --disable-safe-bitstream-reader
#                            disable buffer boundary checking in bitreaders
#                            (faster, but may crash)
#   --sws-max-filter-size=N  the max filter size swscale uses [$sws_max_filter_size_default]

# Optimization options (experts only):
#   --disable-asm            disable all assembly optimizations
#   --disable-altivec        disable AltiVec optimizations
#   --disable-vsx            disable VSX optimizations
#   --disable-power8         disable POWER8 optimizations
#   --disable-amd3dnow       disable 3DNow! optimizations
#   --disable-amd3dnowext    disable 3DNow! extended optimizations
#   --disable-mmx            disable MMX optimizations
#   --disable-mmxext         disable MMXEXT optimizations
#   --disable-sse            disable SSE optimizations
#   --disable-sse2           disable SSE2 optimizations
#   --disable-sse3           disable SSE3 optimizations
#   --disable-ssse3          disable SSSE3 optimizations
#   --disable-sse4           disable SSE4 optimizations
#   --disable-sse42          disable SSE4.2 optimizations
#   --disable-avx            disable AVX optimizations
#   --disable-xop            disable XOP optimizations
#   --disable-fma3           disable FMA3 optimizations
#   --disable-fma4           disable FMA4 optimizations
#   --disable-avx2           disable AVX2 optimizations
#   --disable-avx512         disable AVX-512 optimizations
#   --disable-aesni          disable AESNI optimizations
#   --disable-armv5te        disable armv5te optimizations
#   --disable-armv6          disable armv6 optimizations
#   --disable-armv6t2        disable armv6t2 optimizations
#   --disable-vfp            disable VFP optimizations
#   --disable-neon           disable NEON optimizations
#   --disable-inline-asm     disable use of inline assembly
#   --disable-x86asm         disable use of standalone x86 assembly
#   --disable-mipsdsp        disable MIPS DSP ASE R1 optimizations
#   --disable-mipsdspr2      disable MIPS DSP ASE R2 optimizations
#   --disable-msa            disable MSA optimizations
#   --disable-msa2           disable MSA2 optimizations
#   --disable-mipsfpu        disable floating point MIPS optimizations
#   --disable-mmi            disable Loongson SIMD optimizations
#   --disable-fast-unaligned consider unaligned accesses slow

# Developer options (useful when working on FFmpeg itself):
#   --disable-debug          disable debugging symbols
#   --enable-debug=LEVEL     set the debug level [$debuglevel]
#   --disable-optimizations  disable compiler optimizations
#   --enable-extra-warnings  enable more compiler warnings
#   --disable-stripping      disable stripping of executables and shared libraries
#   --assert-level=level     0(default), 1 or 2, amount of assertion testing,
#                            2 causes a slowdown at runtime.
#   --enable-memory-poisoning fill heap uninitialized allocated space with arbitrary data
#   --valgrind=VALGRIND      run "make fate" tests through valgrind to detect memory
#                            leaks and errors, using the specified valgrind binary.
#                            Cannot be combined with --target-exec
#   --enable-ftrapv          Trap arithmetic overflows
#   --samples=PATH           location of test samples for FATE, if not set use
#                            \$FATE_SAMPLES at make invocation time.
#   --enable-neon-clobber-test check NEON registers for clobbering (should be
#                            used only for debugging purposes)
#   --enable-xmm-clobber-test check XMM registers for clobbering (Win64-only;
#                            should be used only for debugging purposes)
#   --enable-random          randomly enable/disable components
#   --disable-random
#   --enable-random=LIST     randomly enable/disable specific components or
#   --disable-random=LIST    component groups. LIST is a comma-separated list
#                            of NAME[:PROB] entries where NAME is a component
#                            (group) and PROB the probability associated with
#                            NAME (default 0.5).
#   --random-seed=VALUE      seed value for --enable/disable-random
#   --disable-valgrind-backtrace do not print a backtrace under Valgrind
#                            (only applies to --disable-optimizations builds)
#   --enable-ossfuzz         Enable building fuzzer tool
#   --libfuzzer=PATH         path to libfuzzer
#   --ignore-tests=TESTS     comma-separated list (without "fate-" prefix
#                            in the name) of tests whose result is ignored
#   --enable-linux-perf      enable Linux Performance Monitor API

# NOTE: Object files are built at the place where configure is launched.
# EOF
#   exit 0
# }

# if test -t 1 && which tput >/dev/null 2>&1; then
#     ncolors=$(tput colors)
#     if test -n "$ncolors" && test $ncolors -ge 8; then
#         bold_color=$(tput bold)
#         warn_color=$(tput setaf 3)
#         error_color=$(tput setaf 1)
#         reset_color=$(tput sgr0)
#     fi
#     # 72 used instead of 80 since that's the default of pr
#     ncols=$(tput cols)
# fi
# : ${ncols:=72}

# log(){
#     echo "$@" >> $logfile
# }

# log_file(){
#     log BEGIN "$1"
#     log_file_i=1
#     while IFS= read -r log_file_line; do
#         printf '%5d\t%s\n' "$log_file_i" "$log_file_line"
#         log_file_i=$(($log_file_i+1))
#     done < "$1" >> "$logfile"
#     log END "$1"
# }

# warn(){
#     log "WARNING: $*"
#     WARNINGS="${WARNINGS}WARNING: $*\n"
# }

# die(){
#     log "$@"
#     echo "$error_color$bold_color$@$reset_color"
#     cat <<EOF

# If you think configure made a mistake, make sure you are using the latest
# version from Git.  If the latest version fails, report the problem to the
# ffmpeg-user@ffmpeg.org mailing list or IRC #ffmpeg on irc.freenode.net.
# EOF
#     if disabled logging; then
#         cat <<EOF
# Rerun configure with logging enabled (do not use --disable-logging), and
# include the log this produces with your report.
# EOF
#     else
#         cat <<EOF
# Include the log file "$logfile" produced by configure as this will help
# solve the problem.
# EOF
#     fi
#     exit 1
# }

# # Avoid locale weirdness, besides we really just want to translate ASCII.
# toupper(){
#     echo "$@" | tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
# }

# tolower(){
#     echo "$@" | tr ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz
# }

# c_escape(){
#     echo "$*" | sed 's/["\\]/\\\0/g'
# }

# sh_quote(){
#     v=$(echo "$1" | sed "s/'/'\\\\''/g")
#     test "x$v" = "x${v#*[!A-Za-z0-9_/.+-]}" || v="'$v'"
#     echo "$v"
# }

# cleanws(){
#     echo "$@" | sed 's/^ *//;s/[[:space:]][[:space:]]*/ /g;s/ *$//'
# }

# filter(){
#     pat=$1
#     shift
#     for v; do
#         eval "case '$v' in $pat) printf '%s ' '$v' ;; esac"
#     done
# }

# filter_out(){
#     pat=$1
#     shift
#     for v; do
#         eval "case '$v' in $pat) ;; *) printf '%s ' '$v' ;; esac"
#     done
# }

# map(){
#     m=$1
#     shift
#     for v; do eval $m; done
# }

# add_suffix(){
#     suffix=$1
#     shift
#     for v; do echo ${v}${suffix}; done
# }

# remove_suffix(){
#     suffix=$1
#     shift
#     for v; do echo ${v%$suffix}; done
# }

# set_all(){
#     value=$1
#     shift
#     for var in $*; do
#         eval $var=$value
#     done
# }

# set_weak(){
#     value=$1
#     shift
#     for var; do
#         eval : \${$var:=$value}
#     done
# }

# sanitize_var_name(){
#     echo $@ | sed 's/[^A-Za-z0-9_]/_/g'
# }

# set_sanitized(){
#     var=$1
#     shift
#     eval $(sanitize_var_name "$var")='$*'
# }

# get_sanitized(){
#     eval echo \$$(sanitize_var_name "$1")
# }

# pushvar(){
#     for pvar in $*; do
#         eval level=\${${pvar}_level:=0}
#         eval ${pvar}_${level}="\$$pvar"
#         eval ${pvar}_level=$(($level+1))
#     done
# }

# popvar(){
#     for pvar in $*; do
#         eval level=\${${pvar}_level:-0}
#         test $level = 0 && continue
#         eval level=$(($level-1))
#         eval $pvar="\${${pvar}_${level}}"
#         eval ${pvar}_level=$level
#         eval unset ${pvar}_${level}
#     done
# }

# request(){
#     for var in $*; do
#         eval ${var}_requested=yes
#         eval $var=
#     done
# }

# warn_if_gets_disabled(){
#     for var in $*; do
#         WARN_IF_GETS_DISABLED_LIST="$WARN_IF_GETS_DISABLED_LIST $var"
#     done
# }

# enable(){
#     set_all yes $*
# }

# disable(){
#     set_all no $*
# }

# disable_with_reason(){
#     disable $1
#     eval "${1}_disable_reason=\"$2\""
#     if requested $1; then
#         die "ERROR: $1 requested, but $2"
#     fi
# }

# enable_weak(){
#     set_weak yes $*
# }

# disable_weak(){
#     set_weak no $*
# }

# enable_sanitized(){
#     for var; do
#         enable $(sanitize_var_name $var)
#     done
# }

# disable_sanitized(){
#     for var; do
#         disable $(sanitize_var_name $var)
#     done
# }

# do_enable_deep(){
#     for var; do
#         enabled $var && continue
#         set -- $var
#         eval enable_deep \$${var}_select
#         var=$1
#         eval enable_deep_weak \$${var}_suggest
#     done
# }

# enable_deep(){
#     do_enable_deep $*
#     enable $*
# }

# enable_deep_weak(){
#     for var; do
#         disabled $var && continue
#         set -- $var
#         do_enable_deep $var
#         var=$1
#         enable_weak $var
#     done
# }

# requested(){
#     test "${1#!}" = "$1" && op="=" || op="!="
#     eval test "x\$${1#!}_requested" $op "xyes"
# }

# enabled(){
#     test "${1#!}" = "$1" && op="=" || op="!="
#     eval test "x\$${1#!}" $op "xyes"
# }

# disabled(){
#     test "${1#!}" = "$1" && op="=" || op="!="
#     eval test "x\$${1#!}" $op "xno"
# }

# enabled_all(){
#     for opt; do
#         enabled $opt || return 1
#     done
# }

# disabled_all(){
#     for opt; do
#         disabled $opt || return 1
#     done
# }

# enabled_any(){
#     for opt; do
#         enabled $opt && return 0
#     done
# }

# disabled_any(){
#     for opt; do
#         disabled $opt && return 0
#     done
#     return 1
# }

# set_default(){
#     for opt; do
#         eval : \${$opt:=\$${opt}_default}
#     done
# }

# is_in(){
#     value=$1
#     shift
#     for var in $*; do
#         [ $var = $value ] && return 0
#     done
#     return 1
# }

# # The cfg loop is very hot (several thousands iterations), and in bash also
# # potentialy quite slow. Try to abort the iterations early, preferably without
# # calling functions. 70%+ of the time cfg is already done or without deps.
# check_deps(){
#     for cfg; do
#         eval [ x\$${cfg}_checking = xdone ] && continue
#         eval [ x\$${cfg}_checking = xinprogress ] && die "Circular dependency for $cfg."

#         eval "
#         dep_all=\$${cfg}_deps
#         dep_any=\$${cfg}_deps_any
#         dep_con=\$${cfg}_conflict
#         dep_sel=\$${cfg}_select
#         dep_sgs=\$${cfg}_suggest
#         dep_ifa=\$${cfg}_if
#         dep_ifn=\$${cfg}_if_any
#         "

#         # most of the time here $cfg has no deps - avoid costly no-op work
#         if [ "$dep_all$dep_any$dep_con$dep_sel$dep_sgs$dep_ifa$dep_ifn" ]; then
#             eval ${cfg}_checking=inprogress

#             set -- $cfg "$dep_all" "$dep_any" "$dep_con" "$dep_sel" "$dep_sgs" "$dep_ifa" "$dep_ifn"
#             check_deps $dep_all $dep_any $dep_con $dep_sel $dep_sgs $dep_ifa $dep_ifn
#             cfg=$1; dep_all=$2; dep_any=$3; dep_con=$4; dep_sel=$5 dep_sgs=$6; dep_ifa=$7; dep_ifn=$8

#             [ -n "$dep_ifa" ] && { enabled_all $dep_ifa && enable_weak $cfg; }
#             [ -n "$dep_ifn" ] && { enabled_any $dep_ifn && enable_weak $cfg; }
#             enabled_all  $dep_all || { disable_with_reason $cfg "not all dependencies are satisfied: $dep_all"; }
#             enabled_any  $dep_any || { disable_with_reason $cfg "not any dependency is satisfied: $dep_any"; }
#             disabled_all $dep_con || { disable_with_reason $cfg "some conflicting dependencies are unsatisfied: $dep_con"; }
#             disabled_any $dep_sel && { disable_with_reason $cfg "some selected dependency is unsatisfied: $dep_sel"; }

#             enabled $cfg && enable_deep_weak $dep_sel $dep_sgs

#             for dep in $dep_all $dep_any $dep_sel $dep_sgs; do
#                 # filter out library deps, these do not belong in extralibs
#                 is_in $dep $LIBRARY_LIST && continue
#                 enabled $dep && eval append ${cfg}_extralibs ${dep}_extralibs
#             done
#         fi

#         eval ${cfg}_checking=done
#     done
# }

# print_config(){
#     pfx=$1
#     files=$2
#     shift 2
#     map 'eval echo "$v \${$v:-no}"' "$@" |
#     awk "BEGIN { split(\"$files\", files) }
#         {
#             c = \"$pfx\" toupper(\$1);
#             v = \$2;
#             sub(/yes/, 1, v);
#             sub(/no/,  0, v);
#             for (f in files) {
#                 file = files[f];
#                 if (file ~ /\\.h\$/) {
#                     printf(\"#define %s %d\\n\", c, v) >>file;
#                 } else if (file ~ /\\.asm\$/) {
#                     printf(\"%%define %s %d\\n\", c, v) >>file;
#                 } else if (file ~ /\\.mak\$/) {
#                     n = -v ? \"\" : \"!\";
#                     printf(\"%s%s=yes\\n\", n, c) >>file;
#                 } else if (file ~ /\\.texi\$/) {
#                     pre = -v ? \"\" : \"@c \";
#                     yesno = \$2;
#                     c2 = tolower(c);
#                     gsub(/_/, \"-\", c2);
#                     printf(\"%s@set %s %s\\n\", pre, c2, yesno) >>file;
#                 }
#             }
#         }"
# }

# print_enabled(){
#     suf=$1
#     shift
#     for v; do
#         enabled $v && printf "%s\n" ${v%$suf}
#     done
# }

# append(){
#     var=$1
#     shift
#     eval "$var=\"\$$var $*\""
# }

# prepend(){
#     var=$1
#     shift
#     eval "$var=\"$* \$$var\""
# }

# reverse () {
#     eval '
#         reverse_out=
#         for v in $'$1'; do
#             reverse_out="$v $reverse_out"
#         done
#         '$1'=$reverse_out
#     '
# }

# # keeps the last occurence of each non-unique item
# unique(){
#     unique_out=
#     eval unique_in=\$$1
#     reverse unique_in
#     for v in $unique_in; do
#         # " $unique_out" +space such that every item is surrounded with spaces
#         case " $unique_out" in *" $v "*) continue; esac  # already in list
#         unique_out="$unique_out$v "
#     done
#     reverse unique_out
#     eval $1=\$unique_out
# }

# resolve(){
#     resolve_out=
#     eval resolve_in=\$$1
#     for v in $resolve_in; do
#         eval 'resolve_out="$resolve_out$'$v' "'
#     done
#     eval $1=\$resolve_out
# }

# add_cppflags(){
#     append CPPFLAGS "$@"
# }

# add_cflags(){
#     append CFLAGS $($cflags_filter "$@")
# }

# add_cflags_headers(){
#     append CFLAGS_HEADERS $($cflags_filter "$@")
# }

# add_cxxflags(){
#     append CXXFLAGS $($cflags_filter "$@")
# }

# add_objcflags(){
#     append OBJCFLAGS $($objcflags_filter "$@")
# }

# add_asflags(){
#     append ASFLAGS $($asflags_filter "$@")
# }

# add_ldflags(){
#     append LDFLAGS $($ldflags_filter "$@")
# }

# add_ldexeflags(){
#     append LDEXEFLAGS $($ldflags_filter "$@")
# }

# add_ldsoflags(){
#     append LDSOFLAGS $($ldflags_filter "$@")
# }

# add_extralibs(){
#     prepend extralibs $($ldflags_filter "$@")
# }

# add_stripflags(){
#     append ASMSTRIPFLAGS "$@"
# }

# add_host_cppflags(){
#     append host_cppflags "$@"
# }

# add_host_cflags(){
#     append host_cflags $($host_cflags_filter "$@")
# }

# add_host_ldflags(){
#     append host_ldflags $($host_ldflags_filter "$@")
# }

# add_compat(){
#     append compat_objs $1
#     shift
#     map 'add_cppflags -D$v' "$@"
# }

# test_cmd(){
#     log "$@"
#     "$@" >> $logfile 2>&1
# }

# test_stat(){
#     log test_stat "$@"
#     stat "$1" >> $logfile 2>&1
# }

# cc_e(){
#     eval printf '%s\\n' $CC_E
# }

# cc_o(){
#     eval printf '%s\\n' $CC_O
# }

# as_o(){
#     eval printf '%s\\n' $AS_O
# }

# x86asm_o(){
#     eval printf '%s\\n' $X86ASM_O
# }

# ld_o(){
#     eval printf '%s\\n' $LD_O
# }

# hostcc_e(){
#     eval printf '%s\\n' $HOSTCC_E
# }

# hostcc_o(){
#     eval printf '%s\\n' $HOSTCC_O
# }

# nvcc_o(){
#     eval printf '%s\\n' $NVCC_O
# }

# test_cc(){
#     log test_cc "$@"
#     cat > $TMPC
#     log_file $TMPC
#     test_cmd $cc $CPPFLAGS $CFLAGS "$@" $CC_C $(cc_o $TMPO) $TMPC
# }

# test_cxx(){
#     log test_cxx "$@"
#     cat > $TMPCPP
#     log_file $TMPCPP
#     test_cmd $cxx $CPPFLAGS $CFLAGS $CXXFLAGS "$@" $CXX_C -o $TMPO $TMPCPP
# }

# test_objcc(){
#     log test_objcc "$@"
#     cat > $TMPM
#     log_file $TMPM
#     test_cmd $objcc -Werror=missing-prototypes $CPPFLAGS $CFLAGS $OBJCFLAGS "$@" $OBJCC_C $(cc_o $TMPO) $TMPM
# }

# test_nvcc(){
#     log test_nvcc "$@"
#     cat > $TMPCU
#     log_file $TMPCU
#     tmpcu_=$TMPCU
#     tmpo_=$TMPO
#     [ -x "$(command -v cygpath)" ] && tmpcu_=$(cygpath -m $tmpcu_) && tmpo_=$(cygpath -m $tmpo_)
#     test_cmd $nvcc $nvccflags "$@" $NVCC_C $(nvcc_o $tmpo_) $tmpcu_
# }

# check_nvcc() {
#     log check_nvcc "$@"
#     name=$1
#     shift 1
#     disabled $name && return
#     disable $name
#     test_nvcc "$@" <<EOF && enable $name
# extern "C" {
#     __global__ void hello(unsigned char *data) {}
# }
# EOF
# }

# test_cpp(){
#     log test_cpp "$@"
#     cat > $TMPC
#     log_file $TMPC
#     test_cmd $cc $CPPFLAGS $CFLAGS "$@" $(cc_e $TMPO) $TMPC
# }

# test_as(){
#     log test_as "$@"
#     cat > $TMPS
#     log_file $TMPS
#     test_cmd $as $CPPFLAGS $ASFLAGS "$@" $AS_C $(as_o $TMPO) $TMPS
# }

# test_x86asm(){
#     log test_x86asm "$@"
#     echo "$1" > $TMPASM
#     log_file $TMPASM
#     shift
#     test_cmd $x86asmexe $X86ASMFLAGS -Werror "$@" $(x86asm_o $TMPO) $TMPASM
# }

# check_cmd(){
#     log check_cmd "$@"
#     cmd=$1
#     disabled $cmd && return
#     disable $cmd
#     test_cmd $@ && enable $cmd
# }

# check_as(){
#     log check_as "$@"
#     name=$1
#     code=$2
#     shift 2
#     disable $name
#     test_as $@ <<EOF && enable $name
# $code
# EOF
# }

# check_inline_asm(){
#     log check_inline_asm "$@"
#     name="$1"
#     code="$2"
#     shift 2
#     disable $name
#     test_cc "$@" <<EOF && enable $name
# void foo(void){ __asm__ volatile($code); }
# EOF
# }

# check_inline_asm_flags(){
#     log check_inline_asm_flags "$@"
#     name="$1"
#     code="$2"
#     flags=''
#     shift 2
#     while [ "$1" != "" ]; do
#       append flags $1
#       shift
#     done;
#     disable $name
#     cat > $TMPC <<EOF
# void foo(void){ __asm__ volatile($code); }
# EOF
#     log_file $TMPC
#     test_cmd $cc $CPPFLAGS $CFLAGS $flags "$@" $CC_C $(cc_o $TMPO) $TMPC &&
#     enable $name && add_cflags $flags && add_asflags $flags && add_ldflags $flags
# }

# check_insn(){
#     log check_insn "$@"
#     check_inline_asm ${1}_inline "\"$2\""
#     check_as ${1}_external "$2"
# }

# check_x86asm(){
#     log check_x86asm "$@"
#     name=$1
#     shift
#     disable $name
#     test_x86asm "$@" && enable $name
# }

# test_ld(){
#     log test_ld "$@"
#     type=$1
#     shift 1
#     flags=$(filter_out '-l*|*.so' $@)
#     libs=$(filter '-l*|*.so' $@)
#     test_$type $($cflags_filter $flags) || return
#     flags=$($ldflags_filter $flags)
#     libs=$($ldflags_filter $libs)
#     test_cmd $ld $LDFLAGS $LDEXEFLAGS $flags $(ld_o $TMPE) $TMPO $libs $extralibs
# }

# check_ld(){
#     log check_ld "$@"
#     type=$1
#     name=$2
#     shift 2
#     disable $name
#     test_ld $type $@ && enable $name
# }

# print_include(){
#     hdr=$1
#     test "${hdr%.h}" = "${hdr}" &&
#         echo "#include $hdr"    ||
#         echo "#include <$hdr>"
# }

# test_code(){
#     log test_code "$@"
#     check=$1
#     headers=$2
#     code=$3
#     shift 3
#     {
#         for hdr in $headers; do
#             print_include $hdr
#         done
#         echo "int main(void) { $code; return 0; }"
#     } | test_$check "$@"
# }

# check_cppflags(){
#     log check_cppflags "$@"
#     test_cpp "$@" <<EOF && append CPPFLAGS "$@"
# #include <stdlib.h>
# EOF
# }

# test_cflags(){
#     log test_cflags "$@"
#     set -- $($cflags_filter "$@")
#     test_cc "$@" <<EOF
# int x;
# EOF
# }

# check_cflags(){
#     log check_cflags "$@"
#     test_cflags "$@" && add_cflags "$@"
# }

# check_cxxflags(){
#     log check_cxxflags "$@"
#     set -- $($cflags_filter "$@")
#     test_cxx "$@" <<EOF && append CXXFLAGS "$@"
# int x;
# EOF
# }

# test_objcflags(){
#     log test_objcflags "$@"
#     set -- $($objcflags_filter "$@")
#     test_objcc "$@" <<EOF
# int x;
# EOF
# }

# check_objcflags(){
#     log check_objcflags "$@"
#     test_objcflags "$@" && add_objcflags "$@"
# }

# test_ldflags(){
#     log test_ldflags "$@"
#     set -- $($ldflags_filter "$@")
#     test_ld "cc" "$@" <<EOF
# int main(void){ return 0; }
# EOF
# }

# check_ldflags(){
#     log check_ldflags "$@"
#     test_ldflags "$@" && add_ldflags "$@"
# }

# test_stripflags(){
#     log test_stripflags "$@"
#     # call test_cc to get a fresh TMPO
#     test_cc <<EOF
# int main(void) { return 0; }
# EOF
#     test_cmd $strip $ASMSTRIPFLAGS "$@" $TMPO
# }

# check_stripflags(){
#     log check_stripflags "$@"
#     test_stripflags "$@" && add_stripflags "$@"
# }

# check_headers(){
#     log check_headers "$@"
#     headers=$1
#     shift
#     disable_sanitized $headers
#     {
#         for hdr in $headers; do
#             print_include $hdr
#         done
#         echo "int x;"
#     } | test_cpp "$@" && enable_sanitized $headers
# }

# check_header_objcc(){
#     log check_header_objcc "$@"
#     rm -f -- "$TMPO"
#     header=$1
#     shift
#     disable_sanitized $header
#     {
#        echo "#include <$header>"
#        echo "int main(void) { return 0; }"
#     } | test_objcc && test_stat "$TMPO" && enable_sanitized $header
# }

# check_apple_framework(){
#     log check_apple_framework "$@"
#     framework="$1"
#     name="$(tolower $framework)"
#     header="${framework}/${framework}.h"
#     disable $name
#     check_header_objcc $header &&
#         enable $name && eval ${name}_extralibs='"-framework $framework"'
# }

# check_func(){
#     log check_func "$@"
#     func=$1
#     shift
#     disable $func
#     test_ld "cc" "$@" <<EOF && enable $func
# extern int $func();
# int main(void){ $func(); }
# EOF
# }

# check_complexfunc(){
#     log check_complexfunc "$@"
#     func=$1
#     narg=$2
#     shift 2
#     test $narg = 2 && args="f, g" || args="f * I"
#     disable $func
#     test_ld "cc" "$@" <<EOF && enable $func
# #include <complex.h>
# #include <math.h>
# float foo(complex float f, complex float g) { return $func($args); }
# int main(void){ return (int) foo; }
# EOF
# }

# check_mathfunc(){
#     log check_mathfunc "$@"
#     func=$1
#     narg=$2
#     shift 2
#     test $narg = 2 && args="f, g" || args="f"
#     disable $func
#     test_ld "cc" "$@" <<EOF && enable $func
# #include <math.h>
# float foo(float f, float g) { return $func($args); }
# int main(void){ return (int) foo; }
# EOF
# }

# check_func_headers(){
#     log check_func_headers "$@"
#     headers=$1
#     funcs=$2
#     shift 2
#     {
#         for hdr in $headers; do
#             print_include $hdr
#         done
#         echo "#include <stdint.h>"
#         for func in $funcs; do
#             echo "long check_$func(void) { return (long) $func; }"
#         done
#         echo "int main(void) { int ret = 0;"
#         # LTO could optimize out the test functions without this
#         for func in $funcs; do
#             echo " ret |= ((intptr_t)check_$func) & 0xFFFF;"
#         done
#         echo "return ret; }"
#     } | test_ld "cc" "$@" && enable $funcs && enable_sanitized $headers
# }

# check_class_headers_cpp(){
#     log check_class_headers_cpp "$@"
#     headers=$1
#     classes=$2
#     shift 2
#     {
#         for hdr in $headers; do
#             echo "#include <$hdr>"
#         done
#         echo "int main(void) { "
#         i=1
#         for class in $classes; do
#             echo "$class obj$i;"
#             i=$(expr $i + 1)
#         done
#         echo "return 0; }"
#     } | test_ld "cxx" "$@" && enable $funcs && enable_sanitized $headers
# }

# test_cpp_condition(){
#     log test_cpp_condition "$@"
#     header=$1
#     condition=$2
#     shift 2
#     test_cpp "$@" <<EOF
# #include <$header>
# #if !($condition)
# #error "unsatisfied condition: $condition"
# #endif
# EOF
# }

# check_cpp_condition(){
#     log check_cpp_condition "$@"
#     name=$1
#     shift 1
#     disable $name
#     test_cpp_condition "$@" && enable $name
# }

# test_cflags_cc(){
#     log test_cflags_cc "$@"
#     flags=$1
#     header=$2
#     condition=$3
#     shift 3
#     set -- $($cflags_filter "$flags")
#     test_cc "$@" <<EOF
# #include <$header>
# #if !($condition)
# #error "unsatisfied condition: $condition"
# #endif
# EOF
# }

# check_lib(){
#     log check_lib "$@"
#     name="$1"
#     headers="$2"
#     funcs="$3"
#     shift 3
#     disable $name
#     check_func_headers "$headers" "$funcs" "$@" &&
#         enable $name && eval ${name}_extralibs="\$@"
# }

# check_lib_cpp(){
#     log check_lib_cpp "$@"
#     name="$1"
#     headers="$2"
#     classes="$3"
#     shift 3
#     disable $name
#     check_class_headers_cpp "$headers" "$classes" "$@" &&
#         enable $name && eval ${name}_extralibs="\$@"
# }

# test_pkg_config(){
#     log test_pkg_config "$@"
#     name="$1"
#     pkg_version="$2"
#     pkg="${2%% *}"
#     headers="$3"
#     funcs="$4"
#     shift 4
#     disable $name
#     test_cmd $pkg_config --exists --print-errors $pkg_version || return
#     pkg_cflags=$($pkg_config --cflags $pkg_config_flags $pkg)
#     pkg_libs=$($pkg_config --libs $pkg_config_flags $pkg)
#     check_func_headers "$headers" "$funcs" $pkg_cflags $pkg_libs "$@" &&
#         enable $name &&
#         set_sanitized "${name}_cflags"    $pkg_cflags &&
#         set_sanitized "${name}_extralibs" $pkg_libs
# }

# check_pkg_config(){
#     log check_pkg_config "$@"
#     name="$1"
#     test_pkg_config "$@" &&
#         eval add_cflags \$${name}_cflags
# }

# test_exec(){
#     test_ld "cc" "$@" && { enabled cross_compile || $TMPE >> $logfile 2>&1; }
# }

# check_exec_crash(){
#     log check_exec_crash "$@"
#     code=$(cat)

#     # exit() is not async signal safe.  _Exit (C99) and _exit (POSIX)
#     # are safe but may not be available everywhere.  Thus we use
#     # raise(SIGTERM) instead.  The check is run in a subshell so we
#     # can redirect the "Terminated" message from the shell.  SIGBUS
#     # is not defined by standard C so it is used conditionally.

#     (test_exec "$@") >> $logfile 2>&1 <<EOF
# #include <signal.h>
# static void sighandler(int sig){
#     raise(SIGTERM);
# }
# int foo(void){
#     $code
# }
# int (*func_ptr)(void) = foo;
# int main(void){
#     signal(SIGILL, sighandler);
#     signal(SIGFPE, sighandler);
#     signal(SIGSEGV, sighandler);
# #ifdef SIGBUS
#     signal(SIGBUS, sighandler);
# #endif
#     return func_ptr();
# }
# EOF
# }

# check_type(){
#     log check_type "$@"
#     headers=$1
#     type=$2
#     shift 2
#     disable_sanitized "$type"
#     test_code cc "$headers" "$type v" "$@" && enable_sanitized "$type"
# }

# check_struct(){
#     log check_struct "$@"
#     headers=$1
#     struct=$2
#     member=$3
#     shift 3
#     disable_sanitized "${struct}_${member}"
#     test_code cc "$headers" "const void *p = &(($struct *)0)->$member" "$@" &&
#         enable_sanitized "${struct}_${member}"
# }

# check_builtin(){
#     log check_builtin "$@"
#     name=$1
#     headers=$2
#     builtin=$3
#     shift 3
#     disable "$name"
#     test_code ld "$headers" "$builtin" "cc" "$@" && enable "$name"
# }

# check_compile_assert(){
#     log check_compile_assert "$@"
#     name=$1
#     headers=$2
#     condition=$3
#     shift 3
#     disable "$name"
#     test_code cc "$headers" "char c[2 * !!($condition) - 1]" "$@" && enable "$name"
# }

# check_cc(){
#     log check_cc "$@"
#     name=$1
#     shift
#     disable "$name"
#     test_code cc "$@" && enable "$name"
# }

# require(){
#     log require "$@"
#     name_version="$1"
#     name="${1%% *}"
#     shift
#     check_lib $name "$@" || die "ERROR: $name_version not found"
# }

# require_cc(){
#     log require_cc "$@"
#     name="$1"
#     check_cc "$@" || die "ERROR: $name failed"
# }

# require_cpp(){
#     name="$1"
#     headers="$2"
#     classes="$3"
#     shift 3
#     check_lib_cpp "$headers" "$classes" "$@" || die "ERROR: $name not found"
# }

# require_headers(){
#     log require_headers "$@"
#     headers="$1"
#     check_headers "$@" || die "ERROR: $headers not found"
# }

# require_cpp_condition(){
#     log require_cpp_condition "$@"
#     condition="$3"
#     check_cpp_condition "$@" || die "ERROR: $condition not satisfied"
# }

# require_pkg_config(){
#     log require_pkg_config "$@"
#     pkg_version="$2"
#     check_pkg_config "$@" || die "ERROR: $pkg_version not found using pkg-config$pkg_config_fail_message"
# }

# test_host_cc(){
#     log test_host_cc "$@"
#     cat > $TMPC
#     log_file $TMPC
#     test_cmd $host_cc $host_cflags "$@" $HOSTCC_C $(hostcc_o $TMPO) $TMPC
# }

# test_host_cpp(){
#     log test_host_cpp "$@"
#     cat > $TMPC
#     log_file $TMPC
#     test_cmd $host_cc $host_cppflags $host_cflags "$@" $(hostcc_e $TMPO) $TMPC
# }

# check_host_cppflags(){
#     log check_host_cppflags "$@"
#     test_host_cpp "$@" <<EOF && append host_cppflags "$@"
# #include <stdlib.h>
# EOF
# }

# check_host_cflags(){
#     log check_host_cflags "$@"
#     set -- $($host_cflags_filter "$@")
#     test_host_cc "$@" <<EOF && append host_cflags "$@"
# int x;
# EOF
# }

# test_host_cpp_condition(){
#     log test_host_cpp_condition "$@"
#     header=$1
#     condition=$2
#     shift 2
#     test_host_cpp "$@" <<EOF
# #include <$header>
# #if !($condition)
# #error "unsatisfied condition: $condition"
# #endif
# EOF
# }

# check_host_cpp_condition(){
#     log check_host_cpp_condition "$@"
#     name=$1
#     shift 1
#     disable $name
#     test_host_cpp_condition "$@" && enable $name
# }

# cp_if_changed(){
#     cmp -s "$1" "$2" && { test "$quiet" != "yes" && echo "$2 is unchanged"; } && return
#     mkdir -p "$(dirname $2)"
#     cp -f "$1" "$2"
# }

# # CONFIG_LIST contains configurable options, while HAVE_LIST is for
# # system-dependent things.

# AVCODEC_COMPONENTS="
#     bsfs
#     decoders
#     encoders
#     hwaccels
#     parsers
# "

# AVDEVICE_COMPONENTS="
#     indevs
#     outdevs
# "

# AVFILTER_COMPONENTS="
#     filters
# "

# AVFORMAT_COMPONENTS="
#     demuxers
#     muxers
#     protocols
# "

# COMPONENT_LIST="
#     $AVCODEC_COMPONENTS
#     $AVDEVICE_COMPONENTS
#     $AVFILTER_COMPONENTS
#     $AVFORMAT_COMPONENTS
# "

# EXAMPLE_LIST="
#     avio_dir_cmd_example
#     avio_reading_example
#     decode_audio_example
#     decode_video_example
#     demuxing_decoding_example
#     encode_audio_example
#     encode_video_example
#     extract_mvs_example
#     filter_audio_example
#     filtering_audio_example
#     filtering_video_example
#     http_multiclient_example
#     hw_decode_example
#     metadata_example
#     muxing_example
#     qsvdec_example
#     remuxing_example
#     resampling_audio_example
#     scaling_video_example
#     transcode_aac_example
#     transcoding_example
#     vaapi_encode_example
#     vaapi_transcode_example
# "

# EXTERNAL_AUTODETECT_LIBRARY_LIST="
#     alsa
#     appkit
#     avfoundation
#     bzlib
#     coreimage
#     iconv
#     libxcb
#     libxcb_shm
#     libxcb_shape
#     libxcb_xfixes
#     lzma
#     schannel
#     sdl2
#     securetransport
#     sndio
#     xlib
#     zlib
# "

# EXTERNAL_LIBRARY_GPL_LIST="
#     avisynth
#     frei0r
#     libcdio
#     libdavs2
#     librubberband
#     libvidstab
#     libx264
#     libx265
#     libxavs
#     libxavs2
#     libxvid
# "

# EXTERNAL_LIBRARY_NONFREE_LIST="
#     decklink
#     libfdk_aac
#     openssl
#     libtls
# "

# EXTERNAL_LIBRARY_VERSION3_LIST="
#     gmp
#     libaribb24
#     liblensfun
#     libopencore_amrnb
#     libopencore_amrwb
#     libvmaf
#     libvo_amrwbenc
#     mbedtls
#     rkmpp
# "

# EXTERNAL_LIBRARY_GPLV3_LIST="
#     libsmbclient
# "

# EXTERNAL_LIBRARY_LIST="
#     $EXTERNAL_LIBRARY_GPL_LIST
#     $EXTERNAL_LIBRARY_NONFREE_LIST
#     $EXTERNAL_LIBRARY_VERSION3_LIST
#     $EXTERNAL_LIBRARY_GPLV3_LIST
#     chromaprint
#     gcrypt
#     gnutls
#     jni
#     ladspa
#     libaom
#     libass
#     libbluray
#     libbs2b
#     libcaca
#     libcelt
#     libcodec2
#     libdav1d
#     libdc1394
#     libdrm
#     libflite
#     libfontconfig
#     libfreetype
#     libfribidi
#     libgme
#     libgsm
#     libiec61883
#     libilbc
#     libjack
#     libklvanc
#     libkvazaar
#     libmodplug
#     libmp3lame
#     libmysofa
#     libopencv
#     libopenh264
#     libopenjpeg
#     libopenmpt
#     libopus
#     libpulse
#     librsvg
#     librtmp
#     libshine
#     libsmbclient
#     libsnappy
#     libsoxr
#     libspeex
#     libsrt
#     libssh
#     libtensorflow
#     libtesseract
#     libtheora
#     libtwolame
#     libv4l2
#     libvorbis
#     libvpx
#     libwavpack
#     libwebp
#     libxml2
#     libzimg
#     libzmq
#     libzvbi
#     lv2
#     mediacodec
#     openal
#     opengl
#     pocketsphinx
#     vapoursynth
# "

# HWACCEL_AUTODETECT_LIBRARY_LIST="
#     amf
#     audiotoolbox
#     crystalhd
#     cuda
#     cuda_llvm
#     cuvid
#     d3d11va
#     dxva2
#     ffnvcodec
#     nvdec
#     nvenc
#     vaapi
#     vdpau
#     videotoolbox
#     v4l2_m2m
#     xvmc
# "

# # catchall list of things that require external libs to link
# EXTRALIBS_LIST="
#     cpu_init
#     cws2fws
# "

# HWACCEL_LIBRARY_NONFREE_LIST="
#     cuda_nvcc
#     cuda_sdk
#     libnpp
# "

# HWACCEL_LIBRARY_LIST="
#     $HWACCEL_LIBRARY_NONFREE_LIST
#     libmfx
#     mmal
#     omx
#     opencl
# "

# DOCUMENT_LIST="
#     doc
#     htmlpages
#     manpages
#     podpages
#     txtpages
# "

# FEATURE_LIST="
#     ftrapv
#     gray
#     hardcoded_tables
#     omx_rpi
#     runtime_cpudetect
#     safe_bitstream_reader
#     shared
#     small
#     static
#     swscale_alpha
# "

# # this list should be kept in linking order
# LIBRARY_LIST="
#     avdevice
#     avfilter
#     swscale
#     postproc
#     avformat
#     avcodec
#     swresample
#     avresample
#     avutil
# "

# LICENSE_LIST="
#     gpl
#     nonfree
#     version3
# "

# PROGRAM_LIST="
#     ffplay
#     ffprobe
#     ffmpeg
# "

# SUBSYSTEM_LIST="
#     dct
#     dwt
#     error_resilience
#     faan
#     fast_unaligned
#     fft
#     lsp
#     lzo
#     mdct
#     pixelutils
#     network
#     rdft
# "

# # COMPONENT_LIST needs to come last to ensure correct dependency checking
# CONFIG_LIST="
#     $DOCUMENT_LIST
#     $EXAMPLE_LIST
#     $EXTERNAL_LIBRARY_LIST
#     $EXTERNAL_AUTODETECT_LIBRARY_LIST
#     $HWACCEL_LIBRARY_LIST
#     $HWACCEL_AUTODETECT_LIBRARY_LIST
#     $FEATURE_LIST
#     $LICENSE_LIST
#     $LIBRARY_LIST
#     $PROGRAM_LIST
#     $SUBSYSTEM_LIST
#     autodetect
#     fontconfig
#     linux_perf
#     memory_poisoning
#     neon_clobber_test
#     ossfuzz
#     pic
#     thumb
#     valgrind_backtrace
#     xmm_clobber_test
#     $COMPONENT_LIST
# "

# THREADS_LIST="
#     pthreads
#     os2threads
#     w32threads
# "

# ATOMICS_LIST="
#     atomics_gcc
#     atomics_suncc
#     atomics_win32
# "

# AUTODETECT_LIBS="
#     $EXTERNAL_AUTODETECT_LIBRARY_LIST
#     $HWACCEL_AUTODETECT_LIBRARY_LIST
#     $THREADS_LIST
# "

# ARCH_LIST="
#     aarch64
#     alpha
#     arm
#     avr32
#     avr32_ap
#     avr32_uc
#     bfin
#     ia64
#     m68k
#     mips
#     mips64
#     parisc
#     ppc
#     ppc64
#     s390
#     sh4
#     sparc
#     sparc64
#     tilegx
#     tilepro
#     tomi
#     x86
#     x86_32
#     x86_64
# "

# ARCH_EXT_LIST_ARM="
#     armv5te
#     armv6
#     armv6t2
#     armv8
#     neon
#     vfp
#     vfpv3
#     setend
# "

# ARCH_EXT_LIST_MIPS="
#     mipsfpu
#     mips32r2
#     mips32r5
#     mips64r2
#     mips32r6
#     mips64r6
#     mipsdsp
#     mipsdspr2
#     msa
#     msa2
# "

# ARCH_EXT_LIST_LOONGSON="
#     loongson2
#     loongson3
#     mmi
# "

# ARCH_EXT_LIST_X86_SIMD="
#     aesni
#     amd3dnow
#     amd3dnowext
#     avx
#     avx2
#     avx512
#     fma3
#     fma4
#     mmx
#     mmxext
#     sse
#     sse2
#     sse3
#     sse4
#     sse42
#     ssse3
#     xop
# "

# ARCH_EXT_LIST_PPC="
#     altivec
#     dcbzl
#     ldbrx
#     power8
#     ppc4xx
#     vsx
# "

# ARCH_EXT_LIST_X86="
#     $ARCH_EXT_LIST_X86_SIMD
#     cpunop
#     i686
# "

# ARCH_EXT_LIST="
#     $ARCH_EXT_LIST_ARM
#     $ARCH_EXT_LIST_PPC
#     $ARCH_EXT_LIST_X86
#     $ARCH_EXT_LIST_MIPS
#     $ARCH_EXT_LIST_LOONGSON
# "

# ARCH_FEATURES="
#     aligned_stack
#     fast_64bit
#     fast_clz
#     fast_cmov
#     local_aligned
#     simd_align_16
#     simd_align_32
#     simd_align_64
# "

# BUILTIN_LIST="
#     atomic_cas_ptr
#     machine_rw_barrier
#     MemoryBarrier
#     mm_empty
#     rdtsc
#     sem_timedwait
#     sync_val_compare_and_swap
# "
# HAVE_LIST_CMDLINE="
#     inline_asm
#     symver
#     x86asm
# "

# HAVE_LIST_PUB="
#     bigendian
#     fast_unaligned
# "

# HEADERS_LIST="
#     arpa_inet_h
#     asm_types_h
#     cdio_paranoia_h
#     cdio_paranoia_paranoia_h
#     cuda_h
#     dispatch_dispatch_h
#     dev_bktr_ioctl_bt848_h
#     dev_bktr_ioctl_meteor_h
#     dev_ic_bt8xx_h
#     dev_video_bktr_ioctl_bt848_h
#     dev_video_meteor_ioctl_meteor_h
#     direct_h
#     dirent_h
#     dxgidebug_h
#     dxva_h
#     ES2_gl_h
#     gsm_h
#     io_h
#     linux_perf_event_h
#     machine_ioctl_bt848_h
#     machine_ioctl_meteor_h
#     malloc_h
#     opencv2_core_core_c_h
#     OpenGL_gl3_h
#     poll_h
#     sys_param_h
#     sys_resource_h
#     sys_select_h
#     sys_soundcard_h
#     sys_time_h
#     sys_un_h
#     sys_videoio_h
#     termios_h
#     udplite_h
#     unistd_h
#     valgrind_valgrind_h
#     windows_h
#     winsock2_h
# "

# INTRINSICS_LIST="
#     intrinsics_neon
# "

# COMPLEX_FUNCS="
#     cabs
#     cexp
# "

# MATH_FUNCS="
#     atanf
#     atan2f
#     cbrt
#     cbrtf
#     copysign
#     cosf
#     erf
#     exp2
#     exp2f
#     expf
#     hypot
#     isfinite
#     isinf
#     isnan
#     ldexpf
#     llrint
#     llrintf
#     log2
#     log2f
#     log10f
#     lrint
#     lrintf
#     powf
#     rint
#     round
#     roundf
#     sinf
#     trunc
#     truncf
# "

# SYSTEM_FEATURES="
#     dos_paths
#     libc_msvcrt
#     MMAL_PARAMETER_VIDEO_MAX_NUM_CALLBACKS
#     section_data_rel_ro
#     threads
#     uwp
#     winrt
# "

# SYSTEM_FUNCS="
#     access
#     aligned_malloc
#     arc4random
#     clock_gettime
#     closesocket
#     CommandLineToArgvW
#     fcntl
#     getaddrinfo
#     gethrtime
#     getopt
#     GetProcessAffinityMask
#     GetProcessMemoryInfo
#     GetProcessTimes
#     getrusage
#     GetSystemTimeAsFileTime
#     gettimeofday
#     glob
#     glXGetProcAddress
#     gmtime_r
#     inet_aton
#     isatty
#     kbhit
#     localtime_r
#     lstat
#     lzo1x_999_compress
#     mach_absolute_time
#     MapViewOfFile
#     memalign
#     mkstemp
#     mmap
#     mprotect
#     nanosleep
#     PeekNamedPipe
#     posix_memalign
#     pthread_cancel
#     sched_getaffinity
#     SecItemImport
#     SetConsoleTextAttribute
#     SetConsoleCtrlHandler
#     setmode
#     setrlimit
#     Sleep
#     strerror_r
#     sysconf
#     sysctl
#     usleep
#     UTGetOSTypeFromString
#     VirtualAlloc
#     wglGetProcAddress
# "

# SYSTEM_LIBRARIES="
#     bcrypt
#     vaapi_drm
#     vaapi_x11
#     vdpau_x11
# "

# TOOLCHAIN_FEATURES="
#     as_arch_directive
#     as_dn_directive
#     as_fpu_directive
#     as_func
#     as_object_arch
#     asm_mod_q
#     blocks_extension
#     ebp_available
#     ebx_available
#     gnu_as
#     gnu_windres
#     ibm_asm
#     inline_asm_direct_symbol_refs
#     inline_asm_labels
#     inline_asm_nonlocal_labels
#     pragma_deprecated
#     rsync_contimeout
#     symver_asm_label
#     symver_gnu_asm
#     vfp_args
#     xform_asm
#     xmm_clobbers
# "

# TYPES_LIST="
#     kCMVideoCodecType_HEVC
#     kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange
#     kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ
#     kCVImageBufferTransferFunction_ITU_R_2100_HLG
#     kCVImageBufferTransferFunction_Linear
#     socklen_t
#     struct_addrinfo
#     struct_group_source_req
#     struct_ip_mreq_source
#     struct_ipv6_mreq
#     struct_msghdr_msg_flags
#     struct_pollfd
#     struct_rusage_ru_maxrss
#     struct_sctp_event_subscribe
#     struct_sockaddr_in6
#     struct_sockaddr_sa_len
#     struct_sockaddr_storage
#     struct_stat_st_mtim_tv_nsec
#     struct_v4l2_frmivalenum_discrete
# "

# HAVE_LIST="
#     $ARCH_EXT_LIST
#     $(add_suffix _external $ARCH_EXT_LIST)
#     $(add_suffix _inline   $ARCH_EXT_LIST)
#     $ARCH_FEATURES
#     $BUILTIN_LIST
#     $COMPLEX_FUNCS
#     $HAVE_LIST_CMDLINE
#     $HAVE_LIST_PUB
#     $HEADERS_LIST
#     $INTRINSICS_LIST
#     $MATH_FUNCS
#     $SYSTEM_FEATURES
#     $SYSTEM_FUNCS
#     $SYSTEM_LIBRARIES
#     $THREADS_LIST
#     $TOOLCHAIN_FEATURES
#     $TYPES_LIST
#     makeinfo
#     makeinfo_html
#     opencl_d3d11
#     opencl_drm_arm
#     opencl_drm_beignet
#     opencl_dxva2
#     opencl_vaapi_beignet
#     opencl_vaapi_intel_media
#     perl
#     pod2man
#     texi2html
# "

# # options emitted with CONFIG_ prefix but not available on the command line
# CONFIG_EXTRA="
#     aandcttables
#     ac3dsp
#     adts_header
#     audio_frame_queue
#     audiodsp
#     blockdsp
#     bswapdsp
#     cabac
#     cbs
#     cbs_av1
#     cbs_h264
#     cbs_h265
#     cbs_jpeg
#     cbs_mpeg2
#     cbs_vp9
#     dirac_parse
#     dnn
#     dvprofile
#     exif
#     faandct
#     faanidct
#     fdctdsp
#     flacdsp
#     fmtconvert
#     frame_thread_encoder
#     g722dsp
#     golomb
#     gplv3
#     h263dsp
#     h264chroma
#     h264dsp
#     h264parse
#     h264pred
#     h264qpel
#     hevcparse
#     hpeldsp
#     huffman
#     huffyuvdsp
#     huffyuvencdsp
#     idctdsp
#     iirfilter
#     mdct15
#     intrax8
#     iso_media
#     ividsp
#     jpegtables
#     lgplv3
#     libx262
#     llauddsp
#     llviddsp
#     llvidencdsp
#     lpc
#     lzf
#     me_cmp
#     mpeg_er
#     mpegaudio
#     mpegaudiodsp
#     mpegaudioheader
#     mpegvideo
#     mpegvideoenc
#     mss34dsp
#     pixblockdsp
#     qpeldsp
#     qsv
#     qsvdec
#     qsvenc
#     qsvvpp
#     rangecoder
#     riffdec
#     riffenc
#     rtpdec
#     rtpenc_chain
#     rv34dsp
#     scene_sad
#     sinewin
#     snappy
#     srtp
#     startcode
#     texturedsp
#     texturedspenc
#     tpeldsp
#     vaapi_1
#     vaapi_encode
#     vc1dsp
#     videodsp
#     vp3dsp
#     vp56dsp
#     vp8dsp
#     wma_freqs
#     wmv2dsp
# "

# CMDLINE_SELECT="
#     $ARCH_EXT_LIST
#     $CONFIG_LIST
#     $HAVE_LIST_CMDLINE
#     $THREADS_LIST
#     asm
#     cross_compile
#     debug
#     extra_warnings
#     logging
#     lto
#     optimizations
#     rpath
#     stripping
# "

# PATHS_LIST="
#     bindir
#     datadir
#     docdir
#     incdir
#     libdir
#     mandir
#     pkgconfigdir
#     prefix
#     shlibdir
#     install_name_dir
# "

# CMDLINE_SET="
#     $PATHS_LIST
#     ar
#     arch
#     as
#     assert_level
#     build_suffix
#     cc
#     objcc
#     cpu
#     cross_prefix
#     custom_allocator
#     cxx
#     dep_cc
#     doxygen
#     env
#     extra_version
#     gas
#     host_cc
#     host_cflags
#     host_extralibs
#     host_ld
#     host_ldflags
#     host_os
#     ignore_tests
#     install
#     ld
#     ln_s
#     logfile
#     malloc_prefix
#     nm
#     optflags
#     nvcc
#     nvccflags
#     pkg_config
#     pkg_config_flags
#     progs_suffix
#     random_seed
#     ranlib
#     samples
#     strip
#     sws_max_filter_size
#     sysinclude
#     sysroot
#     target_exec
#     target_os
#     target_path
#     target_samples
#     tempprefix
#     toolchain
#     valgrind
#     windres
#     x86asmexe
# "

# CMDLINE_APPEND="
#     extra_cflags
#     extra_cxxflags
#     extra_objcflags
#     host_cppflags
# "

# # code dependency declarations

# # architecture extensions

# armv5te_deps="arm"
# armv6_deps="arm"
# armv6t2_deps="arm"
# armv8_deps="aarch64"
# neon_deps_any="aarch64 arm"
# intrinsics_neon_deps="neon"
# vfp_deps_any="aarch64 arm"
# vfpv3_deps="vfp"
# setend_deps="arm"

# map 'eval ${v}_inline_deps=inline_asm' $ARCH_EXT_LIST_ARM

# altivec_deps="ppc"
# dcbzl_deps="ppc"
# ldbrx_deps="ppc"
# ppc4xx_deps="ppc"
# vsx_deps="altivec"
# power8_deps="vsx"

# loongson2_deps="mips"
# loongson3_deps="mips"
# mips32r2_deps="mips"
# mips32r5_deps="mips"
# mips32r6_deps="mips"
# mips64r2_deps="mips"
# mips64r6_deps="mips"
# mipsfpu_deps="mips"
# mipsdsp_deps="mips"
# mipsdspr2_deps="mips"
# mmi_deps="mips"
# msa_deps="mipsfpu"
# msa2_deps="msa"

# cpunop_deps="i686"
# x86_64_select="i686"
# x86_64_suggest="fast_cmov"

# amd3dnow_deps="mmx"
# amd3dnowext_deps="amd3dnow"
# i686_deps="x86"
# mmx_deps="x86"
# mmxext_deps="mmx"
# sse_deps="mmxext"
# sse2_deps="sse"
# sse3_deps="sse2"
# ssse3_deps="sse3"
# sse4_deps="ssse3"
# sse42_deps="sse4"
# aesni_deps="sse42"
# avx_deps="sse42"
# xop_deps="avx"
# fma3_deps="avx"
# fma4_deps="avx"
# avx2_deps="avx"
# avx512_deps="avx2"

# mmx_external_deps="x86asm"
# mmx_inline_deps="inline_asm x86"
# mmx_suggest="mmx_external mmx_inline"

# for ext in $(filter_out mmx $ARCH_EXT_LIST_X86_SIMD); do
#     eval dep=\$${ext}_deps
#     eval ${ext}_external_deps='"${dep}_external"'
#     eval ${ext}_inline_deps='"${dep}_inline"'
#     eval ${ext}_suggest='"${ext}_external ${ext}_inline"'
# done

# aligned_stack_if_any="aarch64 ppc x86"
# fast_64bit_if_any="aarch64 alpha ia64 mips64 parisc64 ppc64 sparc64 x86_64"
# fast_clz_if_any="aarch64 alpha avr32 mips ppc x86"
# fast_unaligned_if_any="aarch64 ppc x86"
# simd_align_16_if_any="altivec neon sse"
# simd_align_32_if_any="avx"
# simd_align_64_if_any="avx512"

# # system capabilities
# linux_perf_deps="linux_perf_event_h"
# symver_if_any="symver_asm_label symver_gnu_asm"
# valgrind_backtrace_conflict="optimizations"
# valgrind_backtrace_deps="valgrind_valgrind_h"

# # threading support
# atomics_gcc_if="sync_val_compare_and_swap"
# atomics_suncc_if="atomic_cas_ptr machine_rw_barrier"
# atomics_win32_if="MemoryBarrier"
# atomics_native_if_any="$ATOMICS_LIST"
# w32threads_deps="atomics_native"
# threads_if_any="$THREADS_LIST"

# # subsystems
# cbs_av1_select="cbs"
# cbs_h264_select="cbs"
# cbs_h265_select="cbs"
# cbs_jpeg_select="cbs"
# cbs_mpeg2_select="cbs"
# cbs_vp9_select="cbs"
# dct_select="rdft"
# dirac_parse_select="golomb"
# dnn_suggest="libtensorflow"
# error_resilience_select="me_cmp"
# faandct_deps="faan"
# faandct_select="fdctdsp"
# faanidct_deps="faan"
# faanidct_select="idctdsp"
# h264dsp_select="startcode"
# hevcparse_select="golomb"
# frame_thread_encoder_deps="encoders threads"
# intrax8_select="blockdsp idctdsp"
# mdct_select="fft"
# mdct15_select="fft"
# me_cmp_select="fdctdsp idctdsp pixblockdsp"
# mpeg_er_select="error_resilience"
# mpegaudio_select="mpegaudiodsp mpegaudioheader"
# mpegaudiodsp_select="dct"
# mpegvideo_select="blockdsp h264chroma hpeldsp idctdsp me_cmp mpeg_er videodsp"
# mpegvideoenc_select="aandcttables me_cmp mpegvideo pixblockdsp qpeldsp"
# vc1dsp_select="h264chroma qpeldsp startcode"
# rdft_select="fft"

# # decoders / encoders
# aac_decoder_select="adts_header mdct15 mdct sinewin"
# aac_fixed_decoder_select="adts_header mdct sinewin"
# aac_encoder_select="audio_frame_queue iirfilter lpc mdct sinewin"
# aac_latm_decoder_select="aac_decoder aac_latm_parser"
# ac3_decoder_select="ac3_parser ac3dsp bswapdsp fmtconvert mdct"
# ac3_fixed_decoder_select="ac3_parser ac3dsp bswapdsp mdct"
# ac3_encoder_select="ac3dsp audiodsp mdct me_cmp"
# ac3_fixed_encoder_select="ac3dsp audiodsp mdct me_cmp"
# adpcm_g722_decoder_select="g722dsp"
# adpcm_g722_encoder_select="g722dsp"
# aic_decoder_select="golomb idctdsp"
# alac_encoder_select="lpc"
# als_decoder_select="bswapdsp"
# amrnb_decoder_select="lsp"
# amrwb_decoder_select="lsp"
# amv_decoder_select="sp5x_decoder exif"
# amv_encoder_select="jpegtables mpegvideoenc"
# ape_decoder_select="bswapdsp llauddsp"
# apng_decoder_deps="zlib"
# apng_encoder_deps="zlib"
# apng_encoder_select="llvidencdsp"
# aptx_decoder_select="audio_frame_queue"
# aptx_encoder_select="audio_frame_queue"
# aptx_hd_decoder_select="audio_frame_queue"
# aptx_hd_encoder_select="audio_frame_queue"
# asv1_decoder_select="blockdsp bswapdsp idctdsp"
# asv1_encoder_select="aandcttables bswapdsp fdctdsp pixblockdsp"
# asv2_decoder_select="blockdsp bswapdsp idctdsp"
# asv2_encoder_select="aandcttables bswapdsp fdctdsp pixblockdsp"
# atrac1_decoder_select="mdct sinewin"
# atrac3_decoder_select="mdct"
# atrac3p_decoder_select="mdct sinewin"
# atrac9_decoder_select="mdct"
# avrn_decoder_select="exif jpegtables"
# bink_decoder_select="blockdsp hpeldsp"
# binkaudio_dct_decoder_select="mdct rdft dct sinewin wma_freqs"
# binkaudio_rdft_decoder_select="mdct rdft sinewin wma_freqs"
# cavs_decoder_select="blockdsp golomb h264chroma idctdsp qpeldsp videodsp"
# clearvideo_decoder_select="idctdsp"
# cllc_decoder_select="bswapdsp"
# comfortnoise_encoder_select="lpc"
# cook_decoder_select="audiodsp mdct sinewin"
# cscd_decoder_select="lzo"
# cscd_decoder_suggest="zlib"
# dca_decoder_select="mdct"
# dds_decoder_select="texturedsp"
# dirac_decoder_select="dirac_parse dwt golomb videodsp mpegvideoenc"
# dnxhd_decoder_select="blockdsp idctdsp"
# dnxhd_encoder_select="blockdsp fdctdsp idctdsp mpegvideoenc pixblockdsp"
# dolby_e_decoder_select="mdct"
# dvvideo_decoder_select="dvprofile idctdsp"
# dvvideo_encoder_select="dvprofile fdctdsp me_cmp pixblockdsp"
# dxa_decoder_deps="zlib"
# dxv_decoder_select="lzf texturedsp"
# eac3_decoder_select="ac3_decoder"
# eac3_encoder_select="ac3_encoder"
# eamad_decoder_select="aandcttables blockdsp bswapdsp idctdsp mpegvideo"
# eatgq_decoder_select="aandcttables"
# eatqi_decoder_select="aandcttables blockdsp bswapdsp idctdsp"
# exr_decoder_deps="zlib"
# ffv1_decoder_select="rangecoder"
# ffv1_encoder_select="rangecoder"
# ffvhuff_decoder_select="huffyuv_decoder"
# ffvhuff_encoder_select="huffyuv_encoder"
# fic_decoder_select="golomb"
# flac_decoder_select="flacdsp"
# flac_encoder_select="bswapdsp flacdsp lpc"
# flashsv2_decoder_deps="zlib"
# flashsv2_encoder_deps="zlib"
# flashsv_decoder_deps="zlib"
# flashsv_encoder_deps="zlib"
# flv_decoder_select="h263_decoder"
# flv_encoder_select="h263_encoder"
# fourxm_decoder_select="blockdsp bswapdsp"
# fraps_decoder_select="bswapdsp huffman"
# g2m_decoder_deps="zlib"
# g2m_decoder_select="blockdsp idctdsp jpegtables"
# g729_decoder_select="audiodsp"
# h261_decoder_select="mpegvideo"
# h261_encoder_select="mpegvideoenc"
# h263_decoder_select="h263_parser h263dsp mpegvideo qpeldsp"
# h263_encoder_select="h263dsp mpegvideoenc"
# h263i_decoder_select="h263_decoder"
# h263p_decoder_select="h263_decoder"
# h263p_encoder_select="h263_encoder"
# h264_decoder_select="cabac golomb h264chroma h264dsp h264parse h264pred h264qpel videodsp"
# h264_decoder_suggest="error_resilience"
# hap_decoder_select="snappy texturedsp"
# hap_encoder_deps="libsnappy"
# hap_encoder_select="texturedspenc"
# hevc_decoder_select="bswapdsp cabac golomb hevcparse videodsp"
# huffyuv_decoder_select="bswapdsp huffyuvdsp llviddsp"
# huffyuv_encoder_select="bswapdsp huffman huffyuvencdsp llvidencdsp"
# hymt_decoder_select="huffyuv_decoder"
# iac_decoder_select="imc_decoder"
# imc_decoder_select="bswapdsp fft mdct sinewin"
# indeo3_decoder_select="hpeldsp"
# indeo4_decoder_select="ividsp"
# indeo5_decoder_select="ividsp"
# interplay_video_decoder_select="hpeldsp"
# jpegls_decoder_select="mjpeg_decoder"
# jv_decoder_select="blockdsp"
# lagarith_decoder_select="llviddsp"
# ljpeg_encoder_select="idctdsp jpegtables mpegvideoenc"
# lscr_decoder_deps="zlib"
# magicyuv_decoder_select="llviddsp"
# magicyuv_encoder_select="llvidencdsp"
# mdec_decoder_select="blockdsp idctdsp mpegvideo"
# metasound_decoder_select="lsp mdct sinewin"
# mimic_decoder_select="blockdsp bswapdsp hpeldsp idctdsp"
# mjpeg_decoder_select="blockdsp hpeldsp exif idctdsp jpegtables"
# mjpeg_encoder_select="jpegtables mpegvideoenc"
# mjpegb_decoder_select="mjpeg_decoder"
# mlp_decoder_select="mlp_parser"
# mlp_encoder_select="lpc audio_frame_queue"
# motionpixels_decoder_select="bswapdsp"
# mp1_decoder_select="mpegaudio"
# mp1float_decoder_select="mpegaudio"
# mp2_decoder_select="mpegaudio"
# mp2float_decoder_select="mpegaudio"
# mp3_decoder_select="mpegaudio"
# mp3adu_decoder_select="mpegaudio"
# mp3adufloat_decoder_select="mpegaudio"
# mp3float_decoder_select="mpegaudio"
# mp3on4_decoder_select="mpegaudio"
# mp3on4float_decoder_select="mpegaudio"
# mpc7_decoder_select="bswapdsp mpegaudiodsp"
# mpc8_decoder_select="mpegaudiodsp"
# mpegvideo_decoder_select="mpegvideo"
# mpeg1video_decoder_select="mpegvideo"
# mpeg1video_encoder_select="mpegvideoenc h263dsp"
# mpeg2video_decoder_select="mpegvideo"
# mpeg2video_encoder_select="mpegvideoenc h263dsp"
# mpeg4_decoder_select="h263_decoder mpeg4video_parser"
# mpeg4_encoder_select="h263_encoder"
# msa1_decoder_select="mss34dsp"
# mscc_decoder_deps="zlib"
# msmpeg4v1_decoder_select="h263_decoder"
# msmpeg4v2_decoder_select="h263_decoder"
# msmpeg4v2_encoder_select="h263_encoder"
# msmpeg4v3_decoder_select="h263_decoder"
# msmpeg4v3_encoder_select="h263_encoder"
# mss2_decoder_select="mpegvideo qpeldsp vc1_decoder"
# mts2_decoder_select="mss34dsp"
# mwsc_decoder_deps="zlib"
# mxpeg_decoder_select="mjpeg_decoder"
# nellymoser_decoder_select="mdct sinewin"
# nellymoser_encoder_select="audio_frame_queue mdct sinewin"
# nuv_decoder_select="idctdsp lzo"
# on2avc_decoder_select="mdct"
# opus_decoder_deps="swresample"
# opus_decoder_select="mdct15"
# opus_encoder_select="audio_frame_queue mdct15"
# png_decoder_deps="zlib"
# png_encoder_deps="zlib"
# png_encoder_select="llvidencdsp"
# prores_decoder_select="blockdsp idctdsp"
# prores_encoder_select="fdctdsp"
# qcelp_decoder_select="lsp"
# qdm2_decoder_select="mdct rdft mpegaudiodsp"
# ra_144_decoder_select="audiodsp"
# ra_144_encoder_select="audio_frame_queue lpc audiodsp"
# ralf_decoder_select="golomb"
# rasc_decoder_deps="zlib"
# rawvideo_decoder_select="bswapdsp"
# rscc_decoder_deps="zlib"
# rtjpeg_decoder_select="me_cmp"
# rv10_decoder_select="h263_decoder"
# rv10_encoder_select="h263_encoder"
# rv20_decoder_select="h263_decoder"
# rv20_encoder_select="h263_encoder"
# rv30_decoder_select="golomb h264pred h264qpel mpegvideo rv34dsp"
# rv40_decoder_select="golomb h264pred h264qpel mpegvideo rv34dsp"
# screenpresso_decoder_deps="zlib"
# shorten_decoder_select="bswapdsp"
# sipr_decoder_select="lsp"
# snow_decoder_select="dwt h264qpel hpeldsp me_cmp rangecoder videodsp"
# snow_encoder_select="dwt h264qpel hpeldsp me_cmp mpegvideoenc rangecoder"
# sonic_decoder_select="golomb rangecoder"
# sonic_encoder_select="golomb rangecoder"
# sonic_ls_encoder_select="golomb rangecoder"
# sp5x_decoder_select="mjpeg_decoder"
# speedhq_decoder_select="mpegvideo"
# srgc_decoder_deps="zlib"
# svq1_decoder_select="hpeldsp"
# svq1_encoder_select="hpeldsp me_cmp mpegvideoenc"
# svq3_decoder_select="golomb h264dsp h264parse h264pred hpeldsp tpeldsp videodsp"
# svq3_decoder_suggest="zlib"
# tak_decoder_select="audiodsp"
# tdsc_decoder_deps="zlib"
# tdsc_decoder_select="mjpeg_decoder"
# theora_decoder_select="vp3_decoder"
# thp_decoder_select="mjpeg_decoder"
# tiff_decoder_suggest="zlib lzma"
# tiff_encoder_suggest="zlib"
# truehd_decoder_select="mlp_parser"
# truehd_encoder_select="lpc audio_frame_queue"
# truemotion2_decoder_select="bswapdsp"
# truespeech_decoder_select="bswapdsp"
# tscc_decoder_deps="zlib"
# twinvq_decoder_select="mdct lsp sinewin"
# txd_decoder_select="texturedsp"
# utvideo_decoder_select="bswapdsp llviddsp"
# utvideo_encoder_select="bswapdsp huffman llvidencdsp"
# vble_decoder_select="llviddsp"
# vc1_decoder_select="blockdsp h263_decoder h264qpel intrax8 mpegvideo vc1dsp"
# vc1image_decoder_select="vc1_decoder"
# vorbis_decoder_select="mdct"
# vorbis_encoder_select="audio_frame_queue mdct"
# vp3_decoder_select="hpeldsp vp3dsp videodsp"
# vp4_decoder_select="vp3_decoder"
# vp5_decoder_select="h264chroma hpeldsp videodsp vp3dsp vp56dsp"
# vp6_decoder_select="h264chroma hpeldsp huffman videodsp vp3dsp vp56dsp"
# vp6a_decoder_select="vp6_decoder"
# vp6f_decoder_select="vp6_decoder"
# vp7_decoder_select="h264pred videodsp vp8dsp"
# vp8_decoder_select="h264pred videodsp vp8dsp"
# vp9_decoder_select="videodsp vp9_parser vp9_superframe_split_bsf"
# wcmv_decoder_deps="zlib"
# webp_decoder_select="vp8_decoder exif"
# wmalossless_decoder_select="llauddsp"
# wmapro_decoder_select="mdct sinewin wma_freqs"
# wmav1_decoder_select="mdct sinewin wma_freqs"
# wmav1_encoder_select="mdct sinewin wma_freqs"
# wmav2_decoder_select="mdct sinewin wma_freqs"
# wmav2_encoder_select="mdct sinewin wma_freqs"
# wmavoice_decoder_select="lsp rdft dct mdct sinewin"
# wmv1_decoder_select="h263_decoder"
# wmv1_encoder_select="h263_encoder"
# wmv2_decoder_select="blockdsp error_resilience h263_decoder idctdsp intrax8 videodsp wmv2dsp"
# wmv2_encoder_select="h263_encoder wmv2dsp"
# wmv3_decoder_select="vc1_decoder"
# wmv3image_decoder_select="wmv3_decoder"
# xma1_decoder_select="wmapro_decoder"
# xma2_decoder_select="wmapro_decoder"
# zerocodec_decoder_deps="zlib"
# zlib_decoder_deps="zlib"
# zlib_encoder_deps="zlib"
# zmbv_decoder_deps="zlib"
# zmbv_encoder_deps="zlib"

# # hardware accelerators
# crystalhd_deps="libcrystalhd_libcrystalhd_if_h"
# cuda_deps="ffnvcodec"
# cuvid_deps="ffnvcodec"
# d3d11va_deps="dxva_h ID3D11VideoDecoder ID3D11VideoContext"
# dxva2_deps="dxva2api_h DXVA2_ConfigPictureDecode ole32 user32"
# ffnvcodec_deps_any="libdl LoadLibrary"
# nvdec_deps="ffnvcodec"
# vaapi_x11_deps="xlib"
# videotoolbox_hwaccel_deps="videotoolbox pthreads"
# videotoolbox_hwaccel_extralibs="-framework QuartzCore"
# xvmc_deps="X11_extensions_XvMClib_h"

# h263_vaapi_hwaccel_deps="vaapi"
# h263_vaapi_hwaccel_select="h263_decoder"
# h263_videotoolbox_hwaccel_deps="videotoolbox"
# h263_videotoolbox_hwaccel_select="h263_decoder"
# h264_d3d11va_hwaccel_deps="d3d11va"
# h264_d3d11va_hwaccel_select="h264_decoder"
# h264_d3d11va2_hwaccel_deps="d3d11va"
# h264_d3d11va2_hwaccel_select="h264_decoder"
# h264_dxva2_hwaccel_deps="dxva2"
# h264_dxva2_hwaccel_select="h264_decoder"
# h264_nvdec_hwaccel_deps="nvdec"
# h264_nvdec_hwaccel_select="h264_decoder"
# h264_vaapi_hwaccel_deps="vaapi"
# h264_vaapi_hwaccel_select="h264_decoder"
# h264_vdpau_hwaccel_deps="vdpau"
# h264_vdpau_hwaccel_select="h264_decoder"
# h264_videotoolbox_hwaccel_deps="videotoolbox"
# h264_videotoolbox_hwaccel_select="h264_decoder"
# hevc_d3d11va_hwaccel_deps="d3d11va DXVA_PicParams_HEVC"
# hevc_d3d11va_hwaccel_select="hevc_decoder"
# hevc_d3d11va2_hwaccel_deps="d3d11va DXVA_PicParams_HEVC"
# hevc_d3d11va2_hwaccel_select="hevc_decoder"
# hevc_dxva2_hwaccel_deps="dxva2 DXVA_PicParams_HEVC"
# hevc_dxva2_hwaccel_select="hevc_decoder"
# hevc_nvdec_hwaccel_deps="nvdec"
# hevc_nvdec_hwaccel_select="hevc_decoder"
# hevc_vaapi_hwaccel_deps="vaapi VAPictureParameterBufferHEVC"
# hevc_vaapi_hwaccel_select="hevc_decoder"
# hevc_vdpau_hwaccel_deps="vdpau VdpPictureInfoHEVC"
# hevc_vdpau_hwaccel_select="hevc_decoder"
# hevc_videotoolbox_hwaccel_deps="videotoolbox"
# hevc_videotoolbox_hwaccel_select="hevc_decoder"
# mjpeg_nvdec_hwaccel_deps="nvdec"
# mjpeg_nvdec_hwaccel_select="mjpeg_decoder"
# mjpeg_vaapi_hwaccel_deps="vaapi"
# mjpeg_vaapi_hwaccel_select="mjpeg_decoder"
# mpeg_xvmc_hwaccel_deps="xvmc"
# mpeg_xvmc_hwaccel_select="mpeg2video_decoder"
# mpeg1_nvdec_hwaccel_deps="nvdec"
# mpeg1_nvdec_hwaccel_select="mpeg1video_decoder"
# mpeg1_vdpau_hwaccel_deps="vdpau"
# mpeg1_vdpau_hwaccel_select="mpeg1video_decoder"
# mpeg1_videotoolbox_hwaccel_deps="videotoolbox"
# mpeg1_videotoolbox_hwaccel_select="mpeg1video_decoder"
# mpeg1_xvmc_hwaccel_deps="xvmc"
# mpeg1_xvmc_hwaccel_select="mpeg1video_decoder"
# mpeg2_d3d11va_hwaccel_deps="d3d11va"
# mpeg2_d3d11va_hwaccel_select="mpeg2video_decoder"
# mpeg2_d3d11va2_hwaccel_deps="d3d11va"
# mpeg2_d3d11va2_hwaccel_select="mpeg2video_decoder"
# mpeg2_dxva2_hwaccel_deps="dxva2"
# mpeg2_dxva2_hwaccel_select="mpeg2video_decoder"
# mpeg2_nvdec_hwaccel_deps="nvdec"
# mpeg2_nvdec_hwaccel_select="mpeg2video_decoder"
# mpeg2_vaapi_hwaccel_deps="vaapi"
# mpeg2_vaapi_hwaccel_select="mpeg2video_decoder"
# mpeg2_vdpau_hwaccel_deps="vdpau"
# mpeg2_vdpau_hwaccel_select="mpeg2video_decoder"
# mpeg2_videotoolbox_hwaccel_deps="videotoolbox"
# mpeg2_videotoolbox_hwaccel_select="mpeg2video_decoder"
# mpeg2_xvmc_hwaccel_deps="xvmc"
# mpeg2_xvmc_hwaccel_select="mpeg2video_decoder"
# mpeg4_nvdec_hwaccel_deps="nvdec"
# mpeg4_nvdec_hwaccel_select="mpeg4_decoder"
# mpeg4_vaapi_hwaccel_deps="vaapi"
# mpeg4_vaapi_hwaccel_select="mpeg4_decoder"
# mpeg4_vdpau_hwaccel_deps="vdpau"
# mpeg4_vdpau_hwaccel_select="mpeg4_decoder"
# mpeg4_videotoolbox_hwaccel_deps="videotoolbox"
# mpeg4_videotoolbox_hwaccel_select="mpeg4_decoder"
# vc1_d3d11va_hwaccel_deps="d3d11va"
# vc1_d3d11va_hwaccel_select="vc1_decoder"
# vc1_d3d11va2_hwaccel_deps="d3d11va"
# vc1_d3d11va2_hwaccel_select="vc1_decoder"
# vc1_dxva2_hwaccel_deps="dxva2"
# vc1_dxva2_hwaccel_select="vc1_decoder"
# vc1_nvdec_hwaccel_deps="nvdec"
# vc1_nvdec_hwaccel_select="vc1_decoder"
# vc1_vaapi_hwaccel_deps="vaapi"
# vc1_vaapi_hwaccel_select="vc1_decoder"
# vc1_vdpau_hwaccel_deps="vdpau"
# vc1_vdpau_hwaccel_select="vc1_decoder"
# vp8_nvdec_hwaccel_deps="nvdec"
# vp8_nvdec_hwaccel_select="vp8_decoder"
# vp8_vaapi_hwaccel_deps="vaapi"
# vp8_vaapi_hwaccel_select="vp8_decoder"
# vp9_d3d11va_hwaccel_deps="d3d11va DXVA_PicParams_VP9"
# vp9_d3d11va_hwaccel_select="vp9_decoder"
# vp9_d3d11va2_hwaccel_deps="d3d11va DXVA_PicParams_VP9"
# vp9_d3d11va2_hwaccel_select="vp9_decoder"
# vp9_dxva2_hwaccel_deps="dxva2 DXVA_PicParams_VP9"
# vp9_dxva2_hwaccel_select="vp9_decoder"
# vp9_nvdec_hwaccel_deps="nvdec"
# vp9_nvdec_hwaccel_select="vp9_decoder"
# vp9_vaapi_hwaccel_deps="vaapi VADecPictureParameterBufferVP9_bit_depth"
# vp9_vaapi_hwaccel_select="vp9_decoder"
# wmv3_d3d11va_hwaccel_select="vc1_d3d11va_hwaccel"
# wmv3_d3d11va2_hwaccel_select="vc1_d3d11va2_hwaccel"
# wmv3_dxva2_hwaccel_select="vc1_dxva2_hwaccel"
# wmv3_nvdec_hwaccel_select="vc1_nvdec_hwaccel"
# wmv3_vaapi_hwaccel_select="vc1_vaapi_hwaccel"
# wmv3_vdpau_hwaccel_select="vc1_vdpau_hwaccel"

# # hardware-accelerated codecs
# omx_deps="libdl pthreads"
# omx_rpi_select="omx"
# qsv_deps="libmfx"
# qsvdec_select="qsv"
# qsvenc_select="qsv"
# qsvvpp_select="qsv"
# vaapi_encode_deps="vaapi"
# v4l2_m2m_deps="linux_videodev2_h sem_timedwait"

# hwupload_cuda_filter_deps="ffnvcodec"
# scale_npp_filter_deps="ffnvcodec libnpp"
# scale_cuda_filter_deps="ffnvcodec"
# scale_cuda_filter_deps_any="cuda_nvcc cuda_llvm"
# thumbnail_cuda_filter_deps="ffnvcodec"
# thumbnail_cuda_filter_deps_any="cuda_nvcc cuda_llvm"
# transpose_npp_filter_deps="ffnvcodec libnpp"

# amf_deps_any="libdl LoadLibrary"
# nvenc_deps="ffnvcodec"
# nvenc_deps_any="libdl LoadLibrary"
# nvenc_encoder_deps="nvenc"

# h263_v4l2m2m_decoder_deps="v4l2_m2m h263_v4l2_m2m"
# h263_v4l2m2m_encoder_deps="v4l2_m2m h263_v4l2_m2m"
# h264_amf_encoder_deps="amf"
# h264_crystalhd_decoder_select="crystalhd h264_mp4toannexb_bsf h264_parser"
# h264_cuvid_decoder_deps="cuvid"
# h264_cuvid_decoder_select="h264_mp4toannexb_bsf"
# h264_mediacodec_decoder_deps="mediacodec"
# h264_mediacodec_decoder_select="h264_mp4toannexb_bsf h264_parser"
# h264_mmal_decoder_deps="mmal"
# h264_nvenc_encoder_deps="nvenc"
# h264_omx_encoder_deps="omx"
# h264_qsv_decoder_select="h264_mp4toannexb_bsf h264_parser qsvdec"
# h264_qsv_encoder_select="qsvenc"
# h264_rkmpp_decoder_deps="rkmpp"
# h264_rkmpp_decoder_select="h264_mp4toannexb_bsf"
# h264_vaapi_encoder_select="cbs_h264 vaapi_encode"
# h264_v4l2m2m_decoder_deps="v4l2_m2m h264_v4l2_m2m"
# h264_v4l2m2m_decoder_select="h264_mp4toannexb_bsf"
# h264_v4l2m2m_encoder_deps="v4l2_m2m h264_v4l2_m2m"
# hevc_amf_encoder_deps="amf"
# hevc_cuvid_decoder_deps="cuvid"
# hevc_cuvid_decoder_select="hevc_mp4toannexb_bsf"
# hevc_mediacodec_decoder_deps="mediacodec"
# hevc_mediacodec_decoder_select="hevc_mp4toannexb_bsf hevc_parser"
# hevc_nvenc_encoder_deps="nvenc"
# hevc_qsv_decoder_select="hevc_mp4toannexb_bsf hevc_parser qsvdec"
# hevc_qsv_encoder_select="hevcparse qsvenc"
# hevc_rkmpp_decoder_deps="rkmpp"
# hevc_rkmpp_decoder_select="hevc_mp4toannexb_bsf"
# hevc_vaapi_encoder_deps="VAEncPictureParameterBufferHEVC"
# hevc_vaapi_encoder_select="cbs_h265 vaapi_encode"
# hevc_v4l2m2m_decoder_deps="v4l2_m2m hevc_v4l2_m2m"
# hevc_v4l2m2m_decoder_select="hevc_mp4toannexb_bsf"
# hevc_v4l2m2m_encoder_deps="v4l2_m2m hevc_v4l2_m2m"
# mjpeg_cuvid_decoder_deps="cuvid"
# mjpeg_qsv_encoder_deps="libmfx"
# mjpeg_qsv_encoder_select="qsvenc"
# mjpeg_vaapi_encoder_deps="VAEncPictureParameterBufferJPEG"
# mjpeg_vaapi_encoder_select="cbs_jpeg jpegtables vaapi_encode"
# mpeg1_cuvid_decoder_deps="cuvid"
# mpeg1_v4l2m2m_decoder_deps="v4l2_m2m mpeg1_v4l2_m2m"
# mpeg2_crystalhd_decoder_select="crystalhd"
# mpeg2_cuvid_decoder_deps="cuvid"
# mpeg2_mmal_decoder_deps="mmal"
# mpeg2_mediacodec_decoder_deps="mediacodec"
# mpeg2_qsv_decoder_select="qsvdec mpegvideo_parser"
# mpeg2_qsv_encoder_select="qsvenc"
# mpeg2_vaapi_encoder_select="cbs_mpeg2 vaapi_encode"
# mpeg2_v4l2m2m_decoder_deps="v4l2_m2m mpeg2_v4l2_m2m"
# mpeg4_crystalhd_decoder_select="crystalhd"
# mpeg4_cuvid_decoder_deps="cuvid"
# mpeg4_mediacodec_decoder_deps="mediacodec"
# mpeg4_mmal_decoder_deps="mmal"
# mpeg4_omx_encoder_deps="omx"
# mpeg4_v4l2m2m_decoder_deps="v4l2_m2m mpeg4_v4l2_m2m"
# mpeg4_v4l2m2m_encoder_deps="v4l2_m2m mpeg4_v4l2_m2m"
# msmpeg4_crystalhd_decoder_select="crystalhd"
# nvenc_h264_encoder_select="h264_nvenc_encoder"
# nvenc_hevc_encoder_select="hevc_nvenc_encoder"
# vc1_crystalhd_decoder_select="crystalhd"
# vc1_cuvid_decoder_deps="cuvid"
# vc1_mmal_decoder_deps="mmal"
# vc1_qsv_decoder_select="qsvdec vc1_parser"
# vc1_v4l2m2m_decoder_deps="v4l2_m2m vc1_v4l2_m2m"
# vp8_cuvid_decoder_deps="cuvid"
# vp8_mediacodec_decoder_deps="mediacodec"
# vp8_qsv_decoder_select="qsvdec vp8_parser"
# vp8_rkmpp_decoder_deps="rkmpp"
# vp8_vaapi_encoder_deps="VAEncPictureParameterBufferVP8"
# vp8_vaapi_encoder_select="vaapi_encode"
# vp8_v4l2m2m_decoder_deps="v4l2_m2m vp8_v4l2_m2m"
# vp8_v4l2m2m_encoder_deps="v4l2_m2m vp8_v4l2_m2m"
# vp9_cuvid_decoder_deps="cuvid"
# vp9_mediacodec_decoder_deps="mediacodec"
# vp9_rkmpp_decoder_deps="rkmpp"
# vp9_vaapi_encoder_deps="VAEncPictureParameterBufferVP9"
# vp9_vaapi_encoder_select="vaapi_encode"
# vp9_v4l2m2m_decoder_deps="v4l2_m2m vp9_v4l2_m2m"
# wmv3_crystalhd_decoder_select="crystalhd"

# # parsers
# aac_parser_select="adts_header"
# av1_parser_select="cbs_av1"
# h264_parser_select="golomb h264dsp h264parse"
# hevc_parser_select="hevcparse"
# mpegaudio_parser_select="mpegaudioheader"
# mpegvideo_parser_select="mpegvideo"
# mpeg4video_parser_select="h263dsp mpegvideo qpeldsp"
# vc1_parser_select="vc1dsp"

# # bitstream_filters
# aac_adtstoasc_bsf_select="adts_header"
# av1_frame_split_bsf_select="cbs_av1"
# av1_metadata_bsf_select="cbs_av1"
# eac3_core_bsf_select="ac3_parser"
# filter_units_bsf_select="cbs"
# h264_metadata_bsf_deps="const_nan"
# h264_metadata_bsf_select="cbs_h264"
# h264_redundant_pps_bsf_select="cbs_h264"
# hevc_metadata_bsf_select="cbs_h265"
# mjpeg2jpeg_bsf_select="jpegtables"
# mpeg2_metadata_bsf_select="cbs_mpeg2"
# trace_headers_bsf_select="cbs"
# vp9_metadata_bsf_select="cbs_vp9"

# # external libraries
# aac_at_decoder_deps="audiotoolbox"
# aac_at_decoder_select="aac_adtstoasc_bsf"
# ac3_at_decoder_deps="audiotoolbox"
# ac3_at_decoder_select="ac3_parser"
# adpcm_ima_qt_at_decoder_deps="audiotoolbox"
# alac_at_decoder_deps="audiotoolbox"
# amr_nb_at_decoder_deps="audiotoolbox"
# avisynth_deps_any="libdl LoadLibrary"
# avisynth_demuxer_deps="avisynth"
# avisynth_demuxer_select="riffdec"
# eac3_at_decoder_deps="audiotoolbox"
# eac3_at_decoder_select="ac3_parser"
# gsm_ms_at_decoder_deps="audiotoolbox"
# ilbc_at_decoder_deps="audiotoolbox"
# mp1_at_decoder_deps="audiotoolbox"
# mp2_at_decoder_deps="audiotoolbox"
# mp3_at_decoder_deps="audiotoolbox"
# mp1_at_decoder_select="mpegaudioheader"
# mp2_at_decoder_select="mpegaudioheader"
# mp3_at_decoder_select="mpegaudioheader"
# pcm_alaw_at_decoder_deps="audiotoolbox"
# pcm_mulaw_at_decoder_deps="audiotoolbox"
# qdmc_at_decoder_deps="audiotoolbox"
# qdm2_at_decoder_deps="audiotoolbox"
# aac_at_encoder_deps="audiotoolbox"
# aac_at_encoder_select="audio_frame_queue"
# alac_at_encoder_deps="audiotoolbox"
# alac_at_encoder_select="audio_frame_queue"
# ilbc_at_encoder_deps="audiotoolbox"
# ilbc_at_encoder_select="audio_frame_queue"
# pcm_alaw_at_encoder_deps="audiotoolbox"
# pcm_alaw_at_encoder_select="audio_frame_queue"
# pcm_mulaw_at_encoder_deps="audiotoolbox"
# pcm_mulaw_at_encoder_select="audio_frame_queue"
# chromaprint_muxer_deps="chromaprint"
# h264_videotoolbox_encoder_deps="pthreads"
# h264_videotoolbox_encoder_select="videotoolbox_encoder"
# hevc_videotoolbox_encoder_deps="pthreads"
# hevc_videotoolbox_encoder_select="videotoolbox_encoder"
# libaom_av1_decoder_deps="libaom"
# libaom_av1_encoder_deps="libaom"
# libaom_av1_encoder_select="extract_extradata_bsf"
# libaribb24_decoder_deps="libaribb24"
# libcelt_decoder_deps="libcelt"
# libcodec2_decoder_deps="libcodec2"
# libcodec2_encoder_deps="libcodec2"
# libdav1d_decoder_deps="libdav1d"
# libdavs2_decoder_deps="libdavs2"
# libfdk_aac_decoder_deps="libfdk_aac"
# libfdk_aac_encoder_deps="libfdk_aac"
# libfdk_aac_encoder_select="audio_frame_queue"
# libgme_demuxer_deps="libgme"
# libgsm_decoder_deps="libgsm"
# libgsm_encoder_deps="libgsm"
# libgsm_ms_decoder_deps="libgsm"
# libgsm_ms_encoder_deps="libgsm"
# libilbc_decoder_deps="libilbc"
# libilbc_encoder_deps="libilbc"
# libkvazaar_encoder_deps="libkvazaar"
# libmodplug_demuxer_deps="libmodplug"
# libmp3lame_encoder_deps="libmp3lame"
# libmp3lame_encoder_select="audio_frame_queue mpegaudioheader"
# libopencore_amrnb_decoder_deps="libopencore_amrnb"
# libopencore_amrnb_encoder_deps="libopencore_amrnb"
# libopencore_amrnb_encoder_select="audio_frame_queue"
# libopencore_amrwb_decoder_deps="libopencore_amrwb"
# libopenh264_decoder_deps="libopenh264"
# libopenh264_decoder_select="h264_mp4toannexb_bsf"
# libopenh264_encoder_deps="libopenh264"
# libopenjpeg_decoder_deps="libopenjpeg"
# libopenjpeg_encoder_deps="libopenjpeg"
# libopenmpt_demuxer_deps="libopenmpt"
# libopus_decoder_deps="libopus"
# libopus_encoder_deps="libopus"
# libopus_encoder_select="audio_frame_queue"
# librsvg_decoder_deps="librsvg"
# libshine_encoder_deps="libshine"
# libshine_encoder_select="audio_frame_queue"
# libspeex_decoder_deps="libspeex"
# libspeex_encoder_deps="libspeex"
# libspeex_encoder_select="audio_frame_queue"
# libtheora_encoder_deps="libtheora"
# libtwolame_encoder_deps="libtwolame"
# libvo_amrwbenc_encoder_deps="libvo_amrwbenc"
# libvorbis_decoder_deps="libvorbis"
# libvorbis_encoder_deps="libvorbis libvorbisenc"
# libvorbis_encoder_select="audio_frame_queue"
# libvpx_vp8_decoder_deps="libvpx"
# libvpx_vp8_encoder_deps="libvpx"
# libvpx_vp9_decoder_deps="libvpx"
# libvpx_vp9_encoder_deps="libvpx"
# libwavpack_encoder_deps="libwavpack"
# libwavpack_encoder_select="audio_frame_queue"
# libwebp_encoder_deps="libwebp"
# libwebp_anim_encoder_deps="libwebp"
# libx262_encoder_deps="libx262"
# libx264_encoder_deps="libx264"
# libx264rgb_encoder_deps="libx264 x264_csp_bgr"
# libx264rgb_encoder_select="libx264_encoder"
# libx265_encoder_deps="libx265"
# libxavs_encoder_deps="libxavs"
# libxavs2_encoder_deps="libxavs2"
# libxvid_encoder_deps="libxvid"
# libzvbi_teletext_decoder_deps="libzvbi"
# vapoursynth_demuxer_deps="vapoursynth"
# videotoolbox_suggest="coreservices"
# videotoolbox_deps="corefoundation coremedia corevideo"
# videotoolbox_encoder_deps="videotoolbox VTCompressionSessionPrepareToEncodeFrames"

# # demuxers / muxers
# ac3_demuxer_select="ac3_parser"
# aiff_muxer_select="iso_media"
# asf_demuxer_select="riffdec"
# asf_o_demuxer_select="riffdec"
# asf_muxer_select="riffenc"
# asf_stream_muxer_select="asf_muxer"
# avi_demuxer_select="iso_media riffdec exif"
# avi_muxer_select="riffenc"
# caf_demuxer_select="iso_media riffdec"
# caf_muxer_select="iso_media"
# dash_muxer_select="mp4_muxer"
# dash_demuxer_deps="libxml2"
# dirac_demuxer_select="dirac_parser"
# dts_demuxer_select="dca_parser"
# dtshd_demuxer_select="dca_parser"
# dv_demuxer_select="dvprofile"
# dv_muxer_select="dvprofile"
# dxa_demuxer_select="riffdec"
# eac3_demuxer_select="ac3_parser"
# f4v_muxer_select="mov_muxer"
# fifo_muxer_deps="threads"
# flac_demuxer_select="flac_parser"
# hds_muxer_select="flv_muxer"
# hls_muxer_select="mpegts_muxer"
# hls_muxer_suggest="gcrypt openssl"
# image2_alias_pix_demuxer_select="image2_demuxer"
# image2_brender_pix_demuxer_select="image2_demuxer"
# ipod_muxer_select="mov_muxer"
# ismv_muxer_select="mov_muxer"
# ivf_muxer_select="av1_metadata_bsf vp9_superframe_bsf"
# matroska_audio_muxer_select="matroska_muxer"
# matroska_demuxer_select="iso_media riffdec"
# matroska_demuxer_suggest="bzlib lzo zlib"
# matroska_muxer_select="iso_media riffenc"
# mmf_muxer_select="riffenc"
# mov_demuxer_select="iso_media riffdec"
# mov_demuxer_suggest="zlib"
# mov_muxer_select="iso_media riffenc rtpenc_chain"
# mp3_demuxer_select="mpegaudio_parser"
# mp3_muxer_select="mpegaudioheader"
# mp4_muxer_select="mov_muxer"
# mpegts_demuxer_select="iso_media"
# mpegts_muxer_select="adts_muxer latm_muxer"
# mpegtsraw_demuxer_select="mpegts_demuxer"
# mxf_d10_muxer_select="mxf_muxer"
# mxf_opatom_muxer_select="mxf_muxer"
# nut_muxer_select="riffenc"
# nuv_demuxer_select="riffdec"
# oga_muxer_select="ogg_muxer"
# ogg_demuxer_select="dirac_parse"
# ogv_muxer_select="ogg_muxer"
# opus_muxer_select="ogg_muxer"
# psp_muxer_select="mov_muxer"
# rtp_demuxer_select="sdp_demuxer"
# rtp_muxer_select="golomb"
# rtpdec_select="asf_demuxer jpegtables mov_demuxer mpegts_demuxer rm_demuxer rtp_protocol srtp"
# rtsp_demuxer_select="http_protocol rtpdec"
# rtsp_muxer_select="rtp_muxer http_protocol rtp_protocol rtpenc_chain"
# sap_demuxer_select="sdp_demuxer"
# sap_muxer_select="rtp_muxer rtp_protocol rtpenc_chain"
# sdp_demuxer_select="rtpdec"
# smoothstreaming_muxer_select="ismv_muxer"
# spdif_demuxer_select="adts_header"
# spdif_muxer_select="adts_header"
# spx_muxer_select="ogg_muxer"
# swf_demuxer_suggest="zlib"
# tak_demuxer_select="tak_parser"
# tg2_muxer_select="mov_muxer"
# tgp_muxer_select="mov_muxer"
# vobsub_demuxer_select="mpegps_demuxer"
# w64_demuxer_select="wav_demuxer"
# w64_muxer_select="wav_muxer"
# wav_demuxer_select="riffdec"
# wav_muxer_select="riffenc"
# webm_muxer_select="iso_media riffenc"
# webm_dash_manifest_demuxer_select="matroska_demuxer"
# wtv_demuxer_select="mpegts_demuxer riffdec"
# wtv_muxer_select="mpegts_muxer riffenc"
# xmv_demuxer_select="riffdec"
# xwma_demuxer_select="riffdec"

# # indevs / outdevs
# android_camera_indev_deps="android camera2ndk mediandk pthreads"
# android_camera_indev_extralibs="-landroid -lcamera2ndk -lmediandk"
# alsa_indev_deps="alsa"
# alsa_outdev_deps="alsa"
# avfoundation_indev_deps="avfoundation corevideo coremedia pthreads"
# avfoundation_indev_suggest="coregraphics applicationservices"
# avfoundation_indev_extralibs="-framework Foundation"
# bktr_indev_deps_any="dev_bktr_ioctl_bt848_h machine_ioctl_bt848_h dev_video_bktr_ioctl_bt848_h dev_ic_bt8xx_h"
# caca_outdev_deps="libcaca"
# decklink_deps_any="libdl LoadLibrary"
# decklink_indev_deps="decklink threads"
# decklink_indev_extralibs="-lstdc++"
# decklink_outdev_deps="decklink threads"
# decklink_outdev_suggest="libklvanc"
# decklink_outdev_extralibs="-lstdc++"
# dshow_indev_deps="IBaseFilter"
# dshow_indev_extralibs="-lpsapi -lole32 -lstrmiids -luuid -loleaut32 -lshlwapi"
# fbdev_indev_deps="linux_fb_h"
# fbdev_outdev_deps="linux_fb_h"
# gdigrab_indev_deps="CreateDIBSection"
# gdigrab_indev_extralibs="-lgdi32"
# gdigrab_indev_select="bmp_decoder"
# iec61883_indev_deps="libiec61883"
# jack_indev_deps="libjack"
# jack_indev_deps_any="sem_timedwait dispatch_dispatch_h"
# kmsgrab_indev_deps="libdrm"
# lavfi_indev_deps="avfilter"
# libcdio_indev_deps="libcdio"
# libdc1394_indev_deps="libdc1394"
# openal_indev_deps="openal"
# opengl_outdev_deps="opengl"
# opengl_outdev_suggest="sdl2"
# oss_indev_deps_any="sys_soundcard_h"
# oss_outdev_deps_any="sys_soundcard_h"
# pulse_indev_deps="libpulse"
# pulse_outdev_deps="libpulse"
# sdl2_outdev_deps="sdl2"
# sndio_indev_deps="sndio"
# sndio_outdev_deps="sndio"
# v4l2_indev_deps_any="linux_videodev2_h sys_videoio_h"
# v4l2_indev_suggest="libv4l2"
# v4l2_outdev_deps_any="linux_videodev2_h sys_videoio_h"
# v4l2_outdev_suggest="libv4l2"
# vfwcap_indev_deps="vfw32 vfwcap_defines"
# xcbgrab_indev_deps="libxcb"
# xcbgrab_indev_suggest="libxcb_shm libxcb_shape libxcb_xfixes"
# xv_outdev_deps="xlib"

# # protocols
# async_protocol_deps="threads"
# bluray_protocol_deps="libbluray"
# ffrtmpcrypt_protocol_conflict="librtmp_protocol"
# ffrtmpcrypt_protocol_deps_any="gcrypt gmp openssl mbedtls"
# ffrtmpcrypt_protocol_select="tcp_protocol"
# ffrtmphttp_protocol_conflict="librtmp_protocol"
# ffrtmphttp_protocol_select="http_protocol"
# ftp_protocol_select="tcp_protocol"
# gopher_protocol_select="network"
# http_protocol_select="tcp_protocol"
# http_protocol_suggest="zlib"
# httpproxy_protocol_select="tcp_protocol"
# httpproxy_protocol_suggest="zlib"
# https_protocol_select="tls_protocol"
# https_protocol_suggest="zlib"
# icecast_protocol_select="http_protocol"
# mmsh_protocol_select="http_protocol"
# mmst_protocol_select="network"
# rtmp_protocol_conflict="librtmp_protocol"
# rtmp_protocol_select="tcp_protocol"
# rtmp_protocol_suggest="zlib"
# rtmpe_protocol_select="ffrtmpcrypt_protocol"
# rtmpe_protocol_suggest="zlib"
# rtmps_protocol_conflict="librtmp_protocol"
# rtmps_protocol_select="tls_protocol"
# rtmps_protocol_suggest="zlib"
# rtmpt_protocol_select="ffrtmphttp_protocol"
# rtmpt_protocol_suggest="zlib"
# rtmpte_protocol_select="ffrtmpcrypt_protocol ffrtmphttp_protocol"
# rtmpte_protocol_suggest="zlib"
# rtmpts_protocol_select="ffrtmphttp_protocol https_protocol"
# rtmpts_protocol_suggest="zlib"
# rtp_protocol_select="udp_protocol"
# schannel_conflict="openssl gnutls libtls mbedtls"
# sctp_protocol_deps="struct_sctp_event_subscribe struct_msghdr_msg_flags"
# sctp_protocol_select="network"
# securetransport_conflict="openssl gnutls libtls mbedtls"
# srtp_protocol_select="rtp_protocol srtp"
# tcp_protocol_select="network"
# tls_protocol_deps_any="gnutls openssl schannel securetransport libtls mbedtls"
# tls_protocol_select="tcp_protocol"
# udp_protocol_select="network"
# udplite_protocol_select="network"
# unix_protocol_deps="sys_un_h"
# unix_protocol_select="network"

# # external library protocols
# librtmp_protocol_deps="librtmp"
# librtmpe_protocol_deps="librtmp"
# librtmps_protocol_deps="librtmp"
# librtmpt_protocol_deps="librtmp"
# librtmpte_protocol_deps="librtmp"
# libsmbclient_protocol_deps="libsmbclient gplv3"
# libsrt_protocol_deps="libsrt"
# libsrt_protocol_select="network"
# libssh_protocol_deps="libssh"
# libtls_conflict="openssl gnutls mbedtls"

# # filters
# afftdn_filter_deps="avcodec"
# afftdn_filter_select="fft"
# afftfilt_filter_deps="avcodec"
# afftfilt_filter_select="fft"
# afir_filter_deps="avcodec"
# afir_filter_select="fft"
# amovie_filter_deps="avcodec avformat"
# aresample_filter_deps="swresample"
# asr_filter_deps="pocketsphinx"
# ass_filter_deps="libass"
# atempo_filter_deps="avcodec"
# atempo_filter_select="rdft"
# avgblur_opencl_filter_deps="opencl"
# azmq_filter_deps="libzmq"
# blackframe_filter_deps="gpl"
# bm3d_filter_deps="avcodec"
# bm3d_filter_select="dct"
# boxblur_filter_deps="gpl"
# boxblur_opencl_filter_deps="opencl gpl"
# bs2b_filter_deps="libbs2b"
# colorkey_opencl_filter_deps="opencl"
# colormatrix_filter_deps="gpl"
# convolution_opencl_filter_deps="opencl"
# convolve_filter_deps="avcodec"
# convolve_filter_select="fft"
# coreimage_filter_deps="coreimage appkit"
# coreimage_filter_extralibs="-framework OpenGL"
# coreimagesrc_filter_deps="coreimage appkit"
# coreimagesrc_filter_extralibs="-framework OpenGL"
# cover_rect_filter_deps="avcodec avformat gpl"
# cropdetect_filter_deps="gpl"
# deconvolve_filter_deps="avcodec"
# deconvolve_filter_select="fft"
# deinterlace_qsv_filter_deps="libmfx"
# deinterlace_vaapi_filter_deps="vaapi"
# delogo_filter_deps="gpl"
# denoise_vaapi_filter_deps="vaapi"
# derain_filter_select="dnn"
# deshake_filter_select="pixelutils"
# dilation_opencl_filter_deps="opencl"
# drawtext_filter_deps="libfreetype"
# drawtext_filter_suggest="libfontconfig libfribidi"
# elbg_filter_deps="avcodec"
# eq_filter_deps="gpl"
# erosion_opencl_filter_deps="opencl"
# fftfilt_filter_deps="avcodec"
# fftfilt_filter_select="rdft"
# fftdnoiz_filter_deps="avcodec"
# fftdnoiz_filter_select="fft"
# find_rect_filter_deps="avcodec avformat gpl"
# firequalizer_filter_deps="avcodec"
# firequalizer_filter_select="rdft"
# flite_filter_deps="libflite"
# framerate_filter_select="scene_sad"
# freezedetect_filter_select="scene_sad"
# frei0r_filter_deps="frei0r libdl"
# frei0r_src_filter_deps="frei0r libdl"
# fspp_filter_deps="gpl"
# geq_filter_deps="gpl"
# histeq_filter_deps="gpl"
# hqdn3d_filter_deps="gpl"
# interlace_filter_deps="gpl"
# kerndeint_filter_deps="gpl"
# ladspa_filter_deps="ladspa libdl"
# lensfun_filter_deps="liblensfun version3"
# lv2_filter_deps="lv2"
# mcdeint_filter_deps="avcodec gpl"
# movie_filter_deps="avcodec avformat"
# mpdecimate_filter_deps="gpl"
# mpdecimate_filter_select="pixelutils"
# minterpolate_filter_select="scene_sad"
# mptestsrc_filter_deps="gpl"
# negate_filter_deps="lut_filter"
# nlmeans_opencl_filter_deps="opencl"
# nnedi_filter_deps="gpl"
# ocr_filter_deps="libtesseract"
# ocv_filter_deps="libopencv"
# openclsrc_filter_deps="opencl"
# overlay_opencl_filter_deps="opencl"
# overlay_qsv_filter_deps="libmfx"
# overlay_qsv_filter_select="qsvvpp"
# owdenoise_filter_deps="gpl"
# pan_filter_deps="swresample"
# perspective_filter_deps="gpl"
# phase_filter_deps="gpl"
# pp7_filter_deps="gpl"
# pp_filter_deps="gpl postproc"
# prewitt_opencl_filter_deps="opencl"
# procamp_vaapi_filter_deps="vaapi"
# program_opencl_filter_deps="opencl"
# pullup_filter_deps="gpl"
# removelogo_filter_deps="avcodec avformat swscale"
# repeatfields_filter_deps="gpl"
# resample_filter_deps="avresample"
# roberts_opencl_filter_deps="opencl"
# rubberband_filter_deps="librubberband"
# sab_filter_deps="gpl swscale"
# scale2ref_filter_deps="swscale"
# scale_filter_deps="swscale"
# scale_qsv_filter_deps="libmfx"
# select_filter_select="scene_sad"
# sharpness_vaapi_filter_deps="vaapi"
# showcqt_filter_deps="avcodec avformat swscale"
# showcqt_filter_suggest="libfontconfig libfreetype"
# showcqt_filter_select="fft"
# showfreqs_filter_deps="avcodec"
# showfreqs_filter_select="fft"
# showspectrum_filter_deps="avcodec"
# showspectrum_filter_select="fft"
# showspectrumpic_filter_deps="avcodec"
# showspectrumpic_filter_select="fft"
# signature_filter_deps="gpl avcodec avformat"
# smartblur_filter_deps="gpl swscale"
# sobel_opencl_filter_deps="opencl"
# sofalizer_filter_deps="libmysofa avcodec"
# sofalizer_filter_select="fft"
# spectrumsynth_filter_deps="avcodec"
# spectrumsynth_filter_select="fft"
# spp_filter_deps="gpl avcodec"
# spp_filter_select="fft idctdsp fdctdsp me_cmp pixblockdsp"
# sr_filter_deps="avformat swscale"
# sr_filter_select="dnn"
# stereo3d_filter_deps="gpl"
# subtitles_filter_deps="avformat avcodec libass"
# super2xsai_filter_deps="gpl"
# pixfmts_super2xsai_test_deps="super2xsai_filter"
# tinterlace_filter_deps="gpl"
# tinterlace_merge_test_deps="tinterlace_filter"
# tinterlace_pad_test_deps="tinterlace_filter"
# tonemap_filter_deps="const_nan"
# tonemap_opencl_filter_deps="opencl const_nan"
# transpose_opencl_filter_deps="opencl"
# transpose_vaapi_filter_deps="vaapi VAProcPipelineCaps_rotation_flags"
# unsharp_opencl_filter_deps="opencl"
# uspp_filter_deps="gpl avcodec"
# vaguedenoiser_filter_deps="gpl"
# vidstabdetect_filter_deps="libvidstab"
# vidstabtransform_filter_deps="libvidstab"
# libvmaf_filter_deps="libvmaf pthreads"
# zmq_filter_deps="libzmq"
# zoompan_filter_deps="swscale"
# zscale_filter_deps="libzimg const_nan"
# scale_vaapi_filter_deps="vaapi"
# vpp_qsv_filter_deps="libmfx"
# vpp_qsv_filter_select="qsvvpp"
# yadif_cuda_filter_deps="ffnvcodec"
# yadif_cuda_filter_deps_any="cuda_nvcc cuda_llvm"

# # examples
# avio_dir_cmd_deps="avformat avutil"
# avio_reading_deps="avformat avcodec avutil"
# decode_audio_example_deps="avcodec avutil"
# decode_video_example_deps="avcodec avutil"
# demuxing_decoding_example_deps="avcodec avformat avutil"
# encode_audio_example_deps="avcodec avutil"
# encode_video_example_deps="avcodec avutil"
# extract_mvs_example_deps="avcodec avformat avutil"
# filter_audio_example_deps="avfilter avutil"
# filtering_audio_example_deps="avfilter avcodec avformat avutil"
# filtering_video_example_deps="avfilter avcodec avformat avutil"
# http_multiclient_example_deps="avformat avutil fork"
# hw_decode_example_deps="avcodec avformat avutil"
# metadata_example_deps="avformat avutil"
# muxing_example_deps="avcodec avformat avutil swscale"
# qsvdec_example_deps="avcodec avutil libmfx h264_qsv_decoder"
# remuxing_example_deps="avcodec avformat avutil"
# resampling_audio_example_deps="avutil swresample"
# scaling_video_example_deps="avutil swscale"
# transcode_aac_example_deps="avcodec avformat swresample"
# transcoding_example_deps="avfilter avcodec avformat avutil"
# vaapi_encode_example_deps="avcodec avutil h264_vaapi_encoder"
# vaapi_transcode_example_deps="avcodec avformat avutil h264_vaapi_encoder"

# # EXTRALIBS_LIST
# cpu_init_extralibs="pthreads_extralibs"
# cws2fws_extralibs="zlib_extralibs"

# # libraries, in any order
# avcodec_deps="avutil"
# avcodec_suggest="libm"
# avcodec_select="null_bsf"
# avdevice_deps="avformat avcodec avutil"
# avdevice_suggest="libm"
# avfilter_deps="avutil"
# avfilter_suggest="libm"
# avformat_deps="avcodec avutil"
# avformat_suggest="libm network zlib"
# avresample_deps="avutil"
# avresample_suggest="libm"
# avutil_suggest="clock_gettime ffnvcodec libm libdrm libmfx opencl user32 vaapi videotoolbox corefoundation corevideo coremedia bcrypt"
# postproc_deps="avutil gpl"
# postproc_suggest="libm"
# swresample_deps="avutil"
# swresample_suggest="libm libsoxr"
# swscale_deps="avutil"
# swscale_suggest="libm"

# avcodec_extralibs="pthreads_extralibs iconv_extralibs dxva2_extralibs"
# avfilter_extralibs="pthreads_extralibs"
# avutil_extralibs="d3d11va_extralibs nanosleep_extralibs pthreads_extralibs vaapi_drm_extralibs vaapi_x11_extralibs vdpau_x11_extralibs"

# # programs
# ffmpeg_deps="avcodec avfilter avformat"
# ffmpeg_select="aformat_filter anull_filter atrim_filter format_filter
#                hflip_filter null_filter
#                transpose_filter trim_filter vflip_filter"
# ffmpeg_suggest="ole32 psapi shell32"
# ffplay_deps="avcodec avformat swscale swresample sdl2"
# ffplay_select="rdft crop_filter transpose_filter hflip_filter vflip_filter rotate_filter"
# ffplay_suggest="shell32"
# ffprobe_deps="avcodec avformat"
# ffprobe_suggest="shell32"

# # documentation
# podpages_deps="perl"
# manpages_deps="perl pod2man"
# htmlpages_deps="perl"
# htmlpages_deps_any="makeinfo_html texi2html"
# txtpages_deps="perl makeinfo"
# doc_deps_any="manpages htmlpages podpages txtpages"

# # default parameters

# logfile="ffbuild/config.log"

# # installation paths
# prefix_default="/usr/local"
# bindir_default='${prefix}/bin'
# datadir_default='${prefix}/share/ffmpeg'
# docdir_default='${prefix}/share/doc/ffmpeg'
# incdir_default='${prefix}/include'
# libdir_default='${prefix}/lib'
# mandir_default='${prefix}/share/man'

# # toolchain
# ar_default="ar"
# cc_default="gcc"
# cxx_default="g++"
# host_cc_default="gcc"
# doxygen_default="doxygen"
# install="install"
# ln_s_default="ln -s -f"
# nm_default="nm -g"
# pkg_config_default=pkg-config
# ranlib_default="ranlib"
# strip_default="strip"
# version_script='--version-script'
# objformat="elf32"
# x86asmexe_default="nasm"
# windres_default="windres"
# striptype="direct"

# # OS
# target_os_default=$(tolower $(uname -s))
# host_os=$target_os_default

# # machine
# if test "$target_os_default" = aix; then
#     arch_default=$(uname -p)
#     strip_default="strip -X32_64"
#     nm_default="nm -g -X32_64"
# else
#     arch_default=$(uname -m)
# fi
# cpu="generic"
# intrinsics="none"

# # configurable options
# enable $PROGRAM_LIST
# enable $DOCUMENT_LIST
# enable $EXAMPLE_LIST
# enable $(filter_out avresample $LIBRARY_LIST)
# enable stripping

# enable asm
# enable debug
# enable doc
# enable faan faandct faanidct
# enable optimizations
# enable runtime_cpudetect
# enable safe_bitstream_reader
# enable static
# enable swscale_alpha
# enable valgrind_backtrace

# sws_max_filter_size_default=256
# set_default sws_max_filter_size

# # internal components are enabled by default
# enable $EXTRALIBS_LIST

# # Avoid external, non-system, libraries getting enabled by dependency resolution
# disable $EXTERNAL_LIBRARY_LIST $HWACCEL_LIBRARY_LIST

# # build settings
# SHFLAGS='-shared -Wl,-soname,$$(@F)'
# LIBPREF="lib"
# LIBSUF=".a"
# FULLNAME='$(NAME)$(BUILDSUF)'
# LIBNAME='$(LIBPREF)$(FULLNAME)$(LIBSUF)'
# SLIBPREF="lib"
# SLIBSUF=".so"
# SLIBNAME='$(SLIBPREF)$(FULLNAME)$(SLIBSUF)'
# SLIBNAME_WITH_VERSION='$(SLIBNAME).$(LIBVERSION)'
# SLIBNAME_WITH_MAJOR='$(SLIBNAME).$(LIBMAJOR)'
# LIB_INSTALL_EXTRA_CMD='$$(RANLIB) "$(LIBDIR)/$(LIBNAME)"'
# SLIB_INSTALL_NAME='$(SLIBNAME_WITH_VERSION)'
# SLIB_INSTALL_LINKS='$(SLIBNAME_WITH_MAJOR) $(SLIBNAME)'
# VERSION_SCRIPT_POSTPROCESS_CMD="cat"

# asflags_filter=echo
# cflags_filter=echo
# ldflags_filter=echo

# AS_C='-c'
# AS_O='-o $@'
# CC_C='-c'
# CC_E='-E -o $@'
# CC_O='-o $@'
# CXX_C='-c'
# CXX_O='-o $@'
# OBJCC_C='-c'
# OBJCC_E='-E -o $@'
# OBJCC_O='-o $@'
# X86ASM_O='-o $@'
# LD_O='-o $@'
# LD_LIB='-l%'
# LD_PATH='-L'
# HOSTCC_C='-c'
# HOSTCC_E='-E -o $@'
# HOSTCC_O='-o $@'
# HOSTLD_O='-o $@'
# NVCC_C='-c'
# NVCC_O='-o $@'

# host_extralibs='-lm'
# host_cflags_filter=echo
# host_ldflags_filter=echo

# target_path='$(CURDIR)'

# # since the object filename is not given with the -MM flag, the compiler
# # is only able to print the basename, and we must add the path ourselves
# DEPCMD='$(DEP$(1)) $(DEP$(1)FLAGS) $($(1)DEP_FLAGS) $< 2>/dev/null | sed -e "/^\#.*/d" -e "s,^[[:space:]]*$(@F),$(@D)/$(@F)," > $(@:.o=.d)'
# DEPFLAGS='-MM'

# mkdir -p ffbuild

# # find source path
# if test -f configure; then
#     source_path=.
# elif test -f src/configure; then
#     source_path=src
# else
#     source_path=$(cd $(dirname "$0"); pwd)
#     case "$source_path" in
#         *[[:blank:]]*) die "Out of tree builds are impossible with whitespace in source path." ;;
#     esac
#     test -e "$source_path/config.h" &&
#         die "Out of tree builds are impossible with config.h in source dir."
# fi

# for v in "$@"; do
#     r=${v#*=}
#     l=${v%"$r"}
#     r=$(sh_quote "$r")
#     FFMPEG_CONFIGURATION="${FFMPEG_CONFIGURATION# } ${l}${r}"
# done

# find_things_extern(){
#     thing=$1
#     pattern=$2
#     file=$source_path/$3
#     out=${4:-$thing}
#     sed -n "s/^[^#]*extern.*$pattern *ff_\([^ ]*\)_$thing;/\1_$out/p" "$file"
# }

# find_filters_extern(){
#     file=$source_path/$1
#     sed -n 's/^extern AVFilter ff_[avfsinkrc]\{2,5\}_\([[:alnum:]_]\{1,\}\);/\1_filter/p' $file
# }

# FILTER_LIST=$(find_filters_extern libavfilter/allfilters.c)
# OUTDEV_LIST=$(find_things_extern muxer AVOutputFormat libavdevice/alldevices.c outdev)
# INDEV_LIST=$(find_things_extern demuxer AVInputFormat libavdevice/alldevices.c indev)
# MUXER_LIST=$(find_things_extern muxer AVOutputFormat libavformat/allformats.c)
# DEMUXER_LIST=$(find_things_extern demuxer AVInputFormat libavformat/allformats.c)
# ENCODER_LIST=$(find_things_extern encoder AVCodec libavcodec/allcodecs.c)
# DECODER_LIST=$(find_things_extern decoder AVCodec libavcodec/allcodecs.c)
# CODEC_LIST="
#     $ENCODER_LIST
#     $DECODER_LIST
# "
# PARSER_LIST=$(find_things_extern parser AVCodecParser libavcodec/parsers.c)
# BSF_LIST=$(find_things_extern bsf AVBitStreamFilter libavcodec/bitstream_filters.c)
# HWACCEL_LIST=$(find_things_extern hwaccel AVHWAccel libavcodec/hwaccels.h)
# PROTOCOL_LIST=$(find_things_extern protocol URLProtocol libavformat/protocols.c)

# AVCODEC_COMPONENTS_LIST="
#     $BSF_LIST
#     $DECODER_LIST
#     $ENCODER_LIST
#     $HWACCEL_LIST
#     $PARSER_LIST
# "

# AVDEVICE_COMPONENTS_LIST="
#     $INDEV_LIST
#     $OUTDEV_LIST
# "

# AVFILTER_COMPONENTS_LIST="
#     $FILTER_LIST
# "

# AVFORMAT_COMPONENTS_LIST="
#     $DEMUXER_LIST
#     $MUXER_LIST
#     $PROTOCOL_LIST
# "

# ALL_COMPONENTS="
#     $AVCODEC_COMPONENTS_LIST
#     $AVDEVICE_COMPONENTS_LIST
#     $AVFILTER_COMPONENTS_LIST
#     $AVFORMAT_COMPONENTS_LIST
# "

# for n in $COMPONENT_LIST; do
#     v=$(toupper ${n%s})_LIST
#     eval enable \$$v
#     eval ${n}_if_any="\$$v"
# done

# enable $ARCH_EXT_LIST

# die_unknown(){
#     echo "Unknown option \"$1\"."
#     echo "See $0 --help for available options."
#     exit 1
# }

# print_in_columns() {
#     tr ' ' '\n' | sort | tr '\r\n' '  ' | awk -v col_width=24 -v width="$ncols" '
#     {
#         num_cols = width > col_width ? int(width / col_width) : 1;
#         num_rows = int((NF + num_cols-1) / num_cols);
#         y = x = 1;
#         for (y = 1; y <= num_rows; y++) {
#             i = y;
#             for (x = 1; x <= num_cols; x++) {
#                 if (i <= NF) {
#                   line = sprintf("%s%-" col_width "s", line, $i);
#                 }
#                 i = i + num_rows;
#             }
#             print line; line = "";
#         }
#     }' | sed 's/ *$//'
# }

# show_list() {
#     suffix=_$1
#     shift
#     echo $* | sed s/$suffix//g | print_in_columns
#     exit 0
# }

# rand_list(){
#     IFS=', '
#     set -- $*
#     unset IFS
#     for thing; do
#         comp=${thing%:*}
#         prob=${thing#$comp}
#         prob=${prob#:}
#         is_in ${comp} $COMPONENT_LIST && eval comp=\$$(toupper ${comp%s})_LIST
#         echo "prob ${prob:-0.5}"
#         printf '%s\n' $comp
#     done
# }

# do_random(){
#     action=$1
#     shift
#     random_seed=$(awk "BEGIN { srand($random_seed); print srand() }")
#     $action $(rand_list "$@" | awk "BEGIN { srand($random_seed) } \$1 == \"prob\" { prob = \$2; next } rand() < prob { print }")
# }

# for opt do
#     optval="${opt#*=}"
#     case "$opt" in
#         --extra-ldflags=*)
#             add_ldflags $optval
#         ;;
#         --extra-ldexeflags=*)
#             add_ldexeflags $optval
#         ;;
#         --extra-ldsoflags=*)
#             add_ldsoflags $optval
#         ;;
#         --extra-ldlibflags=*)
#             warn "The --extra-ldlibflags option is only provided for compatibility and will be\n"\
#                  "removed in the future. Use --extra-ldsoflags instead."
#             add_ldsoflags $optval
#         ;;
#         --extra-libs=*)
#             add_extralibs $optval
#         ;;
#         --disable-devices)
#             disable $INDEV_LIST $OUTDEV_LIST
#         ;;
#         --enable-debug=*)
#             debuglevel="$optval"
#         ;;
#         --disable-programs)
#             disable $PROGRAM_LIST
#         ;;
#         --disable-everything)
#             map 'eval unset \${$(toupper ${v%s})_LIST}' $COMPONENT_LIST
#         ;;
#         --disable-all)
#             map 'eval unset \${$(toupper ${v%s})_LIST}' $COMPONENT_LIST
#             disable $LIBRARY_LIST $PROGRAM_LIST doc
#             enable avutil
#         ;;
#         --enable-random|--disable-random)
#             action=${opt%%-random}
#             do_random ${action#--} $COMPONENT_LIST
#         ;;
#         --enable-random=*|--disable-random=*)
#             action=${opt%%-random=*}
#             do_random ${action#--} $optval
#         ;;
#         --enable-sdl)
#             enable sdl2
#         ;;
#         --enable-*=*|--disable-*=*)
#             eval $(echo "${opt%%=*}" | sed 's/--/action=/;s/-/ thing=/')
#             is_in "${thing}s" $COMPONENT_LIST || die_unknown "$opt"
#             eval list=\$$(toupper $thing)_LIST
#             name=$(echo "${optval}" | sed "s/,/_${thing}|/g")_${thing}
#             list=$(filter "$name" $list)
#             [ "$list" = "" ] && warn "Option $opt did not match anything"
#             test $action = enable && warn_if_gets_disabled $list
#             $action $list
#         ;;
#         --enable-yasm|--disable-yasm)
#             warn "The ${opt} option is only provided for compatibility and will be\n"\
#                  "removed in the future. Use --enable-x86asm / --disable-x86asm instead."
#             test $opt = --enable-yasm && x86asm=yes || x86asm=no
#         ;;
#         --yasmexe=*)
#             warn "The --yasmexe option is only provided for compatibility and will be\n"\
#                  "removed in the future. Use --x86asmexe instead."
#             x86asmexe="$optval"
#         ;;
#         --enable-?*|--disable-?*)
#             eval $(echo "$opt" | sed 's/--/action=/;s/-/ option=/;s/-/_/g')
#             if is_in $option $COMPONENT_LIST; then
#                 test $action = disable && action=unset
#                 eval $action \$$(toupper ${option%s})_LIST
#             elif is_in $option $CMDLINE_SELECT; then
#                 $action $option
#             else
#                 die_unknown $opt
#             fi
#         ;;
#         --list-*)
#             NAME="${opt#--list-}"
#             is_in $NAME $COMPONENT_LIST || die_unknown $opt
#             NAME=${NAME%s}
#             eval show_list $NAME \$$(toupper $NAME)_LIST
#         ;;
#         --help|-h) show_help
#         ;;
#         --quiet|-q) quiet=yes
#         ;;
#         --fatal-warnings) enable fatal_warnings
#         ;;
#         --libfuzzer=*)
#             libfuzzer_path="$optval"
#         ;;
#         *)
#             optname="${opt%%=*}"
#             optname="${optname#--}"
#             optname=$(echo "$optname" | sed 's/-/_/g')
#             if is_in $optname $CMDLINE_SET; then
#                 eval $optname='$optval'
#             elif is_in $optname $CMDLINE_APPEND; then
#                 append $optname "$optval"
#             else
#                 die_unknown $opt
#             fi
#         ;;
#     esac
# done

# for e in $env; do
#     eval "export $e"
# done

# if disabled autodetect; then

#     # Unless iconv is explicitely disabled by the user, we still want to probe
#     # for the iconv from the libc.
#     disabled iconv || enable libc_iconv

#     disable_weak $EXTERNAL_AUTODETECT_LIBRARY_LIST
#     disable_weak $HWACCEL_AUTODETECT_LIBRARY_LIST
# fi
# # Mark specifically enabled, but normally autodetected libraries as requested.
# for lib in $AUTODETECT_LIBS; do
#     enabled $lib && request $lib
# done
# #TODO: switch to $AUTODETECT_LIBS when $THREADS_LIST is supported the same way
# enable_weak $EXTERNAL_AUTODETECT_LIBRARY_LIST
# enable_weak $HWACCEL_AUTODETECT_LIBRARY_LIST

# disabled logging && logfile=/dev/null

# # command line configuration sanity checks

# # we need to build at least one lib type
# if ! enabled_any static shared; then
#     cat <<EOF
# At least one library type must be built.
# Specify --enable-static to build the static libraries or --enable-shared to
# build the shared libraries as well. To only build the shared libraries specify
# --disable-static in addition to --enable-shared.
# EOF
#     exit 1
# fi

# die_license_disabled() {
#     enabled $1 || { enabled $v && die "$v is $1 and --enable-$1 is not specified."; }
# }

# die_license_disabled_gpl() {
#     enabled $1 || { enabled $v && die "$v is incompatible with the gpl and --enable-$1 is not specified."; }
# }

# map "die_license_disabled gpl"      $EXTERNAL_LIBRARY_GPL_LIST $EXTERNAL_LIBRARY_GPLV3_LIST
# map "die_license_disabled version3" $EXTERNAL_LIBRARY_VERSION3_LIST $EXTERNAL_LIBRARY_GPLV3_LIST

# enabled gpl && map "die_license_disabled_gpl nonfree" $EXTERNAL_LIBRARY_NONFREE_LIST
# map "die_license_disabled nonfree" $HWACCEL_LIBRARY_NONFREE_LIST

# enabled version3 && { enabled gpl && enable gplv3 || enable lgplv3; }

# if enabled nonfree; then
#     license="nonfree and unredistributable"
# elif enabled gplv3; then
#     license="GPL version 3 or later"
# elif enabled lgplv3; then
#     license="LGPL version 3 or later"
# elif enabled gpl; then
#     license="GPL version 2 or later"
# else
#     license="LGPL version 2.1 or later"
# fi

# enabled_all gnutls openssl &&
#     die "GnuTLS and OpenSSL must not be enabled at the same time."

# enabled_all gnutls mbedtls &&
#     die "GnuTLS and mbedTLS must not be enabled at the same time."

# enabled_all openssl mbedtls &&
#     die "OpenSSL and mbedTLS must not be enabled at the same time."

# # Disable all the library-specific components if the library itself
# # is disabled, see AVCODEC_LIST and following _LIST variables.

# disable_components(){
#     disabled ${1} && disable $(
#         eval components="\$$(toupper ${1})_COMPONENTS"
#         map 'eval echo \${$(toupper ${v%s})_LIST}' $components
#     )
# }

# map 'disable_components $v' $LIBRARY_LIST

# echo "# $0 $FFMPEG_CONFIGURATION" > $logfile
# set >> $logfile

# test -n "$valgrind" && toolchain="valgrind-memcheck"

# enabled ossfuzz && ! echo $CFLAGS | grep -q -- "-fsanitize="  && ! echo $CFLAGS | grep -q -- "-fcoverage-mapping" &&{
#     add_cflags  -fsanitize=address,undefined -fsanitize-coverage=trace-pc-guard,trace-cmp -fno-omit-frame-pointer
#     add_ldflags -fsanitize=address,undefined -fsanitize-coverage=trace-pc-guard,trace-cmp
# }

# case "$toolchain" in
#     *-asan)
#         cc_default="${toolchain%-asan}"
#         add_cflags  -fsanitize=address
#         add_ldflags -fsanitize=address
#     ;;
#     *-msan)
#         cc_default="${toolchain%-msan}"
#         add_cflags  -fsanitize=memory -fsanitize-memory-track-origins
#         add_ldflags -fsanitize=memory
#     ;;
#     *-tsan)
#         cc_default="${toolchain%-tsan}"
#         add_cflags  -fsanitize=thread
#         add_ldflags -fsanitize=thread
#         case "$toolchain" in
#             gcc-tsan)
#                 add_cflags  -fPIC
#                 add_ldflags -fPIC
#                 ;;
#         esac
#     ;;
#     *-usan)
#         cc_default="${toolchain%-usan}"
#         add_cflags  -fsanitize=undefined
#         add_ldflags -fsanitize=undefined
#     ;;
#     valgrind-*)
#         target_exec_default="valgrind"
#         case "$toolchain" in
#             valgrind-massif)
#                 target_exec_args="--tool=massif --alloc-fn=av_malloc --alloc-fn=av_mallocz --alloc-fn=av_calloc --alloc-fn=av_fast_padded_malloc --alloc-fn=av_fast_malloc --alloc-fn=av_realloc_f --alloc-fn=av_fast_realloc --alloc-fn=av_realloc"
#                 ;;
#             valgrind-memcheck)
#                 target_exec_args="--error-exitcode=1 --malloc-fill=0x2a --track-origins=yes --leak-check=full --gen-suppressions=all --suppressions=$source_path/tests/fate-valgrind.supp"
#                 ;;
#         esac
#     ;;
#     msvc)
#         # Check whether the current MSVC version needs the C99 converter.
#         # From MSVC 2013 (compiler major version 18) onwards, it does actually
#         # support enough of C99 to build ffmpeg. Default to the new
#         # behaviour if the regexp was unable to match anything, since this
#         # successfully parses the version number of existing supported
#         # versions that require the converter (MSVC 2010 and 2012).
#         cl_major_ver=$(cl.exe 2>&1 | sed -n 's/.*Version \([[:digit:]]\{1,\}\)\..*/\1/p')
#         if [ -z "$cl_major_ver" ] || [ $cl_major_ver -ge 18 ]; then
#             cc_default="cl.exe"
#             cxx_default="cl.exe"
#         else
#             die "Unsupported MSVC version (2013 or newer required)"
#         fi
#         ld_default="$source_path/compat/windows/mslink"
#         nm_default="dumpbin.exe -symbols"
#         ar_default="lib.exe"
#         case "$arch" in
#         aarch64|arm64)
#             as_default="armasm64.exe"
#             ;;
#         arm*)
#             as_default="armasm.exe"
#             ;;
#         esac
#         target_os_default="win32"
#         # Use a relative path for TMPDIR. This makes sure all the
#         # ffconf temp files are written with a relative path, avoiding
#         # issues with msys/win32 path conversion for MSVC parameters
#         # such as -Fo<file> or -out:<file>.
#         TMPDIR=.
#     ;;
#     icl)
#         cc_default="icl"
#         ld_default="xilink"
#         nm_default="dumpbin -symbols"
#         ar_default="xilib"
#         target_os_default="win32"
#         TMPDIR=.
#     ;;
#     gcov)
#         add_cflags  -fprofile-arcs -ftest-coverage
#         add_ldflags -fprofile-arcs -ftest-coverage
#     ;;
#     llvm-cov)
#         add_cflags -fprofile-arcs -ftest-coverage
#         add_ldflags --coverage
#     ;;
#     hardened)
#         add_cppflags -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=2
#         add_cflags   -fno-strict-overflow -fstack-protector-all
#         add_ldflags  -Wl,-z,relro -Wl,-z,now
#         add_cflags   -fPIE
#         add_ldexeflags -fPIE -pie
#     ;;
#     ?*)
#         die "Unknown toolchain $toolchain"
#     ;;
# esac

# if test -n "$cross_prefix"; then
#     test -n "$arch" && test -n "$target_os" ||
#         die "Must specify target arch (--arch) and OS (--target-os) when cross-compiling"
#     enable cross_compile
# fi

# set_default target_os
# if test "$target_os" = android; then
#     cc_default="clang"
# fi

# ar_default="${cross_prefix}${ar_default}"
# cc_default="${cross_prefix}${cc_default}"
# cxx_default="${cross_prefix}${cxx_default}"
# nm_default="${cross_prefix}${nm_default}"
# pkg_config_default="${cross_prefix}${pkg_config_default}"
# if ${cross_prefix}${ranlib_default} 2>&1 | grep -q "\-D "; then
#     ranlib_default="${cross_prefix}${ranlib_default} -D"
# else
#     ranlib_default="${cross_prefix}${ranlib_default}"
# fi
# strip_default="${cross_prefix}${strip_default}"
# windres_default="${cross_prefix}${windres_default}"

# sysinclude_default="${sysroot}/usr/include"

# if enabled cuda_sdk; then
#     warn "Option --enable-cuda-sdk is deprecated. Use --enable-cuda-nvcc instead."
#     enable cuda_nvcc
# fi

# if enabled cuda_nvcc; then
#     nvcc_default="nvcc"
#     nvccflags_default="-gencode arch=compute_30,code=sm_30 -O2"
# else
#     nvcc_default="clang"
#     nvccflags_default="--cuda-gpu-arch=sm_30 -O2"
#     NVCC_C=""
# fi

# set_default arch cc cxx doxygen pkg_config ranlib strip sysinclude \
#     target_exec x86asmexe nvcc
# enabled cross_compile || host_cc_default=$cc
# set_default host_cc

# pkg_config_fail_message=""
# if ! $pkg_config --version >/dev/null 2>&1; then
#     warn "$pkg_config not found, library detection may fail."
#     pkg_config=false
# elif is_in -static $cc $LDFLAGS && ! is_in --static $pkg_config $pkg_config_flags; then
#     pkg_config_fail_message="
# Note: When building a static binary, add --pkg-config-flags=\"--static\"."
# fi

# if test $doxygen != $doxygen_default && \
#   ! $doxygen --version >/dev/null 2>&1; then
#     warn "Specified doxygen \"$doxygen\" not found, API documentation will fail to build."
# fi

# exesuf() {
#     case $1 in
#         mingw32*|mingw64*|win32|win64|cygwin*|*-dos|freedos|opendos|os/2*|symbian) echo .exe ;;
#     esac
# }

# EXESUF=$(exesuf $target_os)
# HOSTEXESUF=$(exesuf $host_os)

# # set temporary file name
# : ${TMPDIR:=$TEMPDIR}
# : ${TMPDIR:=$TMP}
# : ${TMPDIR:=/tmp}

# if [ -n "$tempprefix" ] ; then
#     mktemp(){
#         tmpname="$tempprefix.${HOSTNAME}.${UID}"
#         echo "$tmpname"
#         mkdir "$tmpname"
#     }
# elif ! test_cmd mktemp -u XXXXXX; then
#     # simple replacement for missing mktemp
#     # NOT SAFE FOR GENERAL USE
#     mktemp(){
#         tmpname="${2%%XXX*}.${HOSTNAME}.${UID}.$$"
#         echo "$tmpname"
#         mkdir "$tmpname"
#     }
# fi

# FFTMPDIR=$(mktemp -d "${TMPDIR}/ffconf.XXXXXXXX" 2> /dev/null) ||
#     die "Unable to create temporary directory in $TMPDIR."

# tmpfile(){
#     tmp="${FFTMPDIR}/test"$2
#     (set -C; exec > $tmp) 2> /dev/null ||
#         die "Unable to create temporary file in $FFTMPDIR."
#     eval $1=$tmp
# }

# trap 'rm -rf -- "$FFTMPDIR"' EXIT
# trap 'exit 2' INT

# tmpfile TMPASM .asm
# tmpfile TMPC   .c
# tmpfile TMPCPP .cpp
# tmpfile TMPE   $EXESUF
# tmpfile TMPH   .h
# tmpfile TMPM   .m
# tmpfile TMPCU  .cu
# tmpfile TMPO   .o
# tmpfile TMPS   .S
# tmpfile TMPSH  .sh
# tmpfile TMPV   .ver

# unset -f mktemp

# chmod +x $TMPE

# # make sure we can execute files in $TMPDIR
# cat > $TMPSH 2>> $logfile <<EOF
# #! /bin/sh
# EOF
# chmod +x $TMPSH >> $logfile 2>&1
# if ! $TMPSH >> $logfile 2>&1; then
#     cat <<EOF
# Unable to create and execute files in $TMPDIR.  Set the TMPDIR environment
# variable to another directory and make sure that it is not mounted noexec.
# EOF
#     die "Sanity test failed."
# fi

# armasm_flags(){
#     for flag; do
#         case $flag in
#             # Filter out MSVC cl.exe options from cflags that shouldn't
#             # be passed to gas-preprocessor
#             -M[TD]*)                                            ;;
#             *)                  echo $flag                      ;;
#         esac
#    done
# }

# cparser_flags(){
#     for flag; do
#         case $flag in
#             -Wno-switch)             echo -Wno-switch-enum ;;
#             -Wno-format-zero-length) ;;
#             -Wdisabled-optimization) ;;
#             -Wno-pointer-sign)       echo -Wno-other ;;
#             *)                       echo $flag ;;
#         esac
#     done
# }

# msvc_common_flags(){
#     for flag; do
#         case $flag in
#             # In addition to specifying certain flags under the compiler
#             # specific filters, they must be specified here as well or else the
#             # generic catch all at the bottom will print the original flag.
#             -Wall)                ;;
#             -Wextra)              ;;
#             -std=c99)             ;;
#             # Common flags
#             -fomit-frame-pointer) ;;
#             -g)                   echo -Z7 ;;
#             -fno-math-errno)      ;;
#             -fno-common)          ;;
#             -fno-signed-zeros)    ;;
#             -fPIC)                ;;
#             -mthumb)              ;;
#             -march=*)             ;;
#             -lz)                  echo zlib.lib ;;
#             -lx264)               echo libx264.lib ;;
#             -lstdc++)             ;;
#             -l*)                  echo ${flag#-l}.lib ;;
#             -LARGEADDRESSAWARE)   echo $flag ;;
#             -L*)                  echo -libpath:${flag#-L} ;;
#             *)                    echo $flag ;;
#         esac
#     done
# }

# msvc_flags(){
#     msvc_common_flags "$@"
#     for flag; do
#         case $flag in
#             -Wall)                echo -W3 -wd4018 -wd4146 -wd4244 -wd4305     \
#                                        -wd4554 ;;
#             -Wextra)              echo -W4 -wd4244 -wd4127 -wd4018 -wd4389     \
#                                        -wd4146 -wd4057 -wd4204 -wd4706 -wd4305 \
#                                        -wd4152 -wd4324 -we4013 -wd4100 -wd4214 \
#                                        -wd4307 \
#                                        -wd4273 -wd4554 -wd4701 -wd4703 ;;
#         esac
#     done
# }

# icl_flags(){
#     msvc_common_flags "$@"
#     for flag; do
#         case $flag in
#             # Despite what Intel's documentation says -Wall, which is supported
#             # on Windows, does enable remarks so disable them here.
#             -Wall)                echo $flag -Qdiag-disable:remark ;;
#             -std=c99)             echo -Qstd=c99 ;;
#             -flto)                echo -ipo ;;
#         esac
#     done
# }

# icc_flags(){
#     for flag; do
#         case $flag in
#             -flto)                echo -ipo ;;
#             *)                    echo $flag ;;
#         esac
#     done
# }

# suncc_flags(){
#     for flag; do
#         case $flag in
#             -march=*|-mcpu=*)
#                 case "${flag#*=}" in
#                     native)                   echo -xtarget=native       ;;
#                     v9|niagara)               echo -xarch=sparc          ;;
#                     ultrasparc)               echo -xarch=sparcvis       ;;
#                     ultrasparc3|niagara2)     echo -xarch=sparcvis2      ;;
#                     i586|pentium)             echo -xchip=pentium        ;;
#                     i686|pentiumpro|pentium2) echo -xtarget=pentium_pro  ;;
#                     pentium3*|c3-2)           echo -xtarget=pentium3     ;;
#                     pentium-m)          echo -xarch=sse2 -xchip=pentium3 ;;
#                     pentium4*)          echo -xtarget=pentium4           ;;
#                     prescott|nocona)    echo -xarch=sse3 -xchip=pentium4 ;;
#                     *-sse3)             echo -xarch=sse3                 ;;
#                     core2)              echo -xarch=ssse3 -xchip=core2   ;;
#                     bonnell)                   echo -xarch=ssse3         ;;
#                     corei7|nehalem)            echo -xtarget=nehalem     ;;
#                     westmere)                  echo -xtarget=westmere    ;;
#                     silvermont)                echo -xarch=sse4_2        ;;
#                     corei7-avx|sandybridge)    echo -xtarget=sandybridge ;;
#                     core-avx*|ivybridge|haswell|broadwell|skylake*|knl)
#                                                echo -xarch=avx           ;;
#                     amdfam10|barcelona)        echo -xtarget=barcelona   ;;
#                     btver1)                    echo -xarch=amdsse4a      ;;
#                     btver2|bdver*|znver*)      echo -xarch=avx           ;;
#                     athlon-4|athlon-[mx]p)     echo -xarch=ssea          ;;
#                     k8|opteron|athlon64|athlon-fx)
#                                                echo -xarch=sse2a         ;;
#                     athlon*)                   echo -xarch=pentium_proa  ;;
#                 esac
#                 ;;
#             -std=c99)             echo -xc99              ;;
#             -fomit-frame-pointer) echo -xregs=frameptr    ;;
#             -fPIC)                echo -KPIC -xcode=pic32 ;;
#             -W*,*)                echo $flag              ;;
#             -f*-*|-W*|-mimpure-text)                      ;;
#             -shared)              echo -G                 ;;
#             *)                    echo $flag              ;;
#         esac
#     done
# }

# probe_cc(){
#     pfx=$1
#     _cc=$2
#     first=$3

#     unset _type _ident _cc_c _cc_e _cc_o _flags _cflags
#     unset _ld_o _ldflags _ld_lib _ld_path
#     unset _depflags _DEPCMD _DEPFLAGS
#     _flags_filter=echo

#     if $_cc --version 2>&1 | grep -q '^GNU assembler'; then
#         true # no-op to avoid reading stdin in following checks
#     elif $_cc -v 2>&1 | grep -q '^gcc.*LLVM'; then
#         _type=llvm_gcc
#         gcc_extra_ver=$(expr "$($_cc --version 2>/dev/null | head -n1)" : '.*\((.*)\)')
#         _ident="llvm-gcc $($_cc -dumpversion 2>/dev/null) $gcc_extra_ver"
#         _depflags='-MMD -MF $(@:.o=.d) -MT $@'
#         _cflags_speed='-O3'
#         _cflags_size='-Os'
#     elif $_cc -v 2>&1 | grep -qi ^gcc; then
#         _type=gcc
#         gcc_version=$($_cc --version | head -n1)
#         gcc_basever=$($_cc -dumpversion)
#         gcc_pkg_ver=$(expr "$gcc_version" : '[^ ]* \(([^)]*)\)')
#         gcc_ext_ver=$(expr "$gcc_version" : ".*$gcc_pkg_ver $gcc_basever \\(.*\\)")
#         _ident=$(cleanws "gcc $gcc_basever $gcc_pkg_ver $gcc_ext_ver")
#         case $gcc_basever in
#             2) ;;
#             2.*) ;;
#             *) _depflags='-MMD -MF $(@:.o=.d) -MT $@' ;;
#         esac
#         if [ "$first" = true ]; then
#             case $gcc_basever in
#                 4.2*)
#                 warn "gcc 4.2 is outdated and may miscompile FFmpeg. Please use a newer compiler." ;;
#             esac
#         fi
#         _cflags_speed='-O3'
#         _cflags_size='-Os'
#     elif $_cc --version 2>/dev/null | grep -q ^icc; then
#         _type=icc
#         _ident=$($_cc --version | head -n1)
#         _depflags='-MMD'
#         _cflags_speed='-O3'
#         _cflags_size='-Os'
#         _cflags_noopt='-O1'
#         _flags_filter=icc_flags
#     elif $_cc -v 2>&1 | grep -q xlc; then
#         _type=xlc
#         _ident=$($_cc -qversion 2>/dev/null | head -n1)
#         _cflags_speed='-O5'
#         _cflags_size='-O5 -qcompact'
#     elif $_cc --vsn 2>/dev/null | grep -Eq "ARM (C/C\+\+ )?Compiler"; then
#         test -d "$sysroot" || die "No valid sysroot specified."
#         _type=armcc
#         _ident=$($_cc --vsn | grep -i build | head -n1 | sed 's/.*: //')
#         armcc_conf="$PWD/armcc.conf"
#         $_cc --arm_linux_configure                 \
#              --arm_linux_config_file="$armcc_conf" \
#              --configure_sysroot="$sysroot"        \
#              --configure_cpp_headers="$sysinclude" >>$logfile 2>&1 ||
#              die "Error creating armcc configuration file."
#         $_cc --vsn | grep -q RVCT && armcc_opt=rvct || armcc_opt=armcc
#         _flags="--arm_linux_config_file=$armcc_conf --translate_gcc"
#         as_default="${cross_prefix}gcc"
#         _depflags='-MMD'
#         _cflags_speed='-O3'
#         _cflags_size='-Os'
#     elif $_cc -v 2>&1 | grep -q clang && ! $_cc -? > /dev/null 2>&1; then
#         _type=clang
#         _ident=$($_cc --version 2>/dev/null | head -n1)
#         _depflags='-MMD -MF $(@:.o=.d) -MT $@'
#         _cflags_speed='-O3'
#         _cflags_size='-Oz'
#     elif $_cc -V 2>&1 | grep -q Sun; then
#         _type=suncc
#         _ident=$($_cc -V 2>&1 | head -n1 | cut -d' ' -f 2-)
#         _DEPCMD='$(DEP$(1)) $(DEP$(1)FLAGS) $($(1)DEP_FLAGS) $< | sed -e "1s,^.*: ,$@: ," -e "\$$!s,\$$, \\\," -e "1!s,^.*: , ," > $(@:.o=.d)'
#         _DEPFLAGS='-xM1 -xc99'
#         _ldflags='-std=c99'
#         _cflags_speed='-O5'
#         _cflags_size='-O5 -xspace'
#         _flags_filter=suncc_flags
#     elif $_cc -v 2>&1 | grep -q 'PathScale\|Path64'; then
#         _type=pathscale
#         _ident=$($_cc -v 2>&1 | head -n1 | tr -d :)
#         _depflags='-MMD -MF $(@:.o=.d) -MT $@'
#         _cflags_speed='-O2'
#         _cflags_size='-Os'
#         _flags_filter='filter_out -Wdisabled-optimization'
#     elif $_cc -v 2>&1 | grep -q Open64; then
#         _type=open64
#         _ident=$($_cc -v 2>&1 | head -n1 | tr -d :)
#         _depflags='-MMD -MF $(@:.o=.d) -MT $@'
#         _cflags_speed='-O2'
#         _cflags_size='-Os'
#         _flags_filter='filter_out -Wdisabled-optimization|-Wtype-limits|-fno-signed-zeros'
#     elif $_cc 2>&1 | grep -q 'Microsoft.*ARM.*Assembler'; then
#         _type=armasm
#         _ident=$($_cc | head -n1)
#         # 4509: "This form of conditional instruction is deprecated"
#         _flags="-nologo -ignore 4509"
#         _flags_filter=armasm_flags
#     elif $_cc 2>&1 | grep -q Intel; then
#         _type=icl
#         _ident=$($_cc 2>&1 | head -n1)
#         _depflags='-QMMD -QMF$(@:.o=.d) -QMT$@'
#         # Not only is O3 broken on 13.x+ but it is slower on all previous
#         # versions (tested) as well.
#         _cflags_speed="-O2"
#         _cflags_size="-O1 -Oi" # -O1 without -Oi miscompiles stuff
#         if $_cc 2>&1 | grep -q Linker; then
#             _ld_o='-out:$@'
#         else
#             _ld_o='-Fe$@'
#         fi
#         _cc_o='-Fo$@'
#         _cc_e='-P'
#         _flags_filter=icl_flags
#         _ld_lib='lib%.a'
#         _ld_path='-libpath:'
#         # -Qdiag-error to make icl error when seeing certain unknown arguments
#         _flags='-nologo -Qdiag-error:4044,10157'
#         # -Qvec- -Qsimd- to prevent miscompilation, -GS, fp:precise for consistency
#         # with MSVC which enables it by default.
#         _cflags='-Qms0 -Qvec- -Qsimd- -GS -fp:precise'
#         disable stripping
#     elif $_cc -? 2>/dev/null | grep -q 'LLVM.*Linker'; then
#         # lld can emulate multiple different linkers; in ms link.exe mode,
#         # the -? parameter gives the help output which contains an identifyable
#         # string, while it gives an error in other modes.
#         _type=lld-link
#         # The link.exe mode doesn't have a switch for getting the version,
#         # but we can force it back to gnu mode and get the version from there.
#         _ident=$($_cc -flavor gnu --version 2>/dev/null)
#         _ld_o='-out:$@'
#         _flags_filter=msvc_flags
#         _ld_lib='lib%.a'
#         _ld_path='-libpath:'
#     elif $_cc -nologo- 2>&1 | grep -q Microsoft || { $_cc -v 2>&1 | grep -q clang && $_cc -? > /dev/null 2>&1; }; then
#         _type=msvc
#         _ident=$($_cc 2>&1 | head -n1 | tr -d '\r')
#         _DEPCMD='$(DEP$(1)) $(DEP$(1)FLAGS) $($(1)DEP_FLAGS) $< 2>&1 | awk '\''/including/ { sub(/^.*file: */, ""); gsub(/\\/, "/"); if (!match($$0, / /)) print "$@:", $$0 }'\'' > $(@:.o=.d)'
#         _DEPFLAGS='$(CPPFLAGS) $(CFLAGS) -showIncludes -Zs'
#         _cflags_speed="-O2"
#         _cflags_size="-O1"
#         _cflags_noopt="-O1"
#         if $_cc -nologo- 2>&1 | grep -q Linker; then
#             _ld_o='-out:$@'
#         else
#             _ld_o='-Fe$@'
#         fi
#         _cc_o='-Fo$@'
#         _cc_e='-P -Fi$@'
#         _flags_filter=msvc_flags
#         _ld_lib='lib%.a'
#         _ld_path='-libpath:'
#         _flags='-nologo'
#         disable stripping
#     elif $_cc --version 2>/dev/null | grep -q ^cparser; then
#         _type=cparser
#         _ident=$($_cc --version | head -n1)
#         _depflags='-MMD'
#         _cflags_speed='-O4'
#         _cflags_size='-O2'
#         _flags_filter=cparser_flags
#     fi

#     eval ${pfx}_type=\$_type
#     eval ${pfx}_ident=\$_ident
# }

# set_ccvars(){
#     eval ${1}_C=\${_cc_c-\${${1}_C}}
#     eval ${1}_E=\${_cc_e-\${${1}_E}}
#     eval ${1}_O=\${_cc_o-\${${1}_O}}

#     if [ -n "$_depflags" ]; then
#         eval ${1}_DEPFLAGS=\$_depflags
#     else
#         eval ${1}DEP=\${_DEPCMD:-\$DEPCMD}
#         eval ${1}DEP_FLAGS=\${_DEPFLAGS:-\$DEPFLAGS}
#         eval DEP${1}FLAGS=\$_flags
#     fi
# }

# probe_cc cc "$cc" "true"
# cflags_filter=$_flags_filter
# cflags_speed=$_cflags_speed
# cflags_size=$_cflags_size
# cflags_noopt=$_cflags_noopt
# add_cflags $_flags $_cflags
# cc_ldflags=$_ldflags
# set_ccvars CC
# set_ccvars CXX

# probe_cc hostcc "$host_cc"
# host_cflags_filter=$_flags_filter
# host_cflags_speed=$_cflags_speed
# add_host_cflags  $_flags $_cflags
# set_ccvars HOSTCC

# test -n "$cc_type" && enable $cc_type ||
#     warn "Unknown C compiler $cc, unable to select optimal CFLAGS"

# : ${as_default:=$cc}
# : ${objcc_default:=$cc}
# : ${dep_cc_default:=$cc}
# : ${ld_default:=$cc}
# : ${host_ld_default:=$host_cc}
# set_default ar as objcc dep_cc ld ln_s host_ld windres

# probe_cc as "$as"
# asflags_filter=$_flags_filter
# add_asflags $_flags $_cflags
# set_ccvars AS

# probe_cc objcc "$objcc"
# objcflags_filter=$_flags_filter
# add_objcflags $_flags $_cflags
# set_ccvars OBJC

# probe_cc ld "$ld"
# ldflags_filter=$_flags_filter
# add_ldflags $_flags $_ldflags
# test "$cc_type" != "$ld_type" && add_ldflags $cc_ldflags
# LD_O=${_ld_o-$LD_O}
# LD_LIB=${_ld_lib-$LD_LIB}
# LD_PATH=${_ld_path-$LD_PATH}

# probe_cc hostld "$host_ld"
# host_ldflags_filter=$_flags_filter
# add_host_ldflags $_flags $_ldflags
# HOSTLD_O=${_ld_o-$HOSTLD_O}

# if [ -z "$CC_DEPFLAGS" ] && [ "$dep_cc" != "$cc" ]; then
#     probe_cc depcc "$dep_cc"
#     CCDEP=${_DEPCMD:-$DEPCMD}
#     CCDEP_FLAGS=${_DEPFLAGS:=$DEPFLAGS}
#     DEPCCFLAGS=$_flags
# fi

# if $ar 2>&1 | grep -q Microsoft; then
#     arflags="-nologo"
#     ar_o='-out:$@'
# elif $ar 2>&1 | grep -q "\[D\] "; then
#     arflags="rcD"
#     ar_o='$@'
# else
#     arflags="rc"
#     ar_o='$@'
# fi

# add_cflags $extra_cflags
# add_cxxflags $extra_cxxflags
# add_objcflags $extra_objcflags
# add_asflags $extra_cflags

# if test -n "$sysroot"; then
#     case "$cc_type" in
#         gcc|llvm_gcc|clang)
#             add_cppflags --sysroot="$sysroot"
#             add_ldflags --sysroot="$sysroot"
#         ;;
#     esac
# fi

# if test "$cpu" = host; then
#     enabled cross_compile &&
#         die "--cpu=host makes no sense when cross-compiling."

#     case "$cc_type" in
#         gcc|llvm_gcc)
#             check_native(){
#                 $cc $1=native -v -c -o $TMPO $TMPC >$TMPE 2>&1 || return
#                 sed -n "/cc1.*$1=/{
#                             s/.*$1=\\([^ ]*\\).*/\\1/
#                             p
#                             q
#                         }" $TMPE
#             }
#             cpu=$(check_native -march || check_native -mcpu)
#         ;;
#         clang)
#             check_native(){
#                 $cc $1=native -v -c -o $TMPO $TMPC >$TMPE 2>&1 || return
#                 sed -n "/cc1.*-target-cpu /{
#                             s/.*-target-cpu \\([^ ]*\\).*/\\1/
#                             p
#                             q
#                         }" $TMPE
#             }
#             cpu=$(check_native -march)
#         ;;
#     esac

#     test "${cpu:-host}" = host &&
#         die "--cpu=host not supported with compiler $cc"
# fi

# # Deal with common $arch aliases
# case "$arch" in
#     aarch64|arm64)
#         arch="aarch64"
#     ;;
#     arm*|iPad*|iPhone*)
#         arch="arm"
#     ;;
#     mips*|IP*)
#         case "$arch" in
#         *el)
#             add_cppflags -EL
#             add_ldflags -EL
#         ;;
#         *eb)
#             add_cppflags -EB
#             add_ldflags -EB
#         ;;
#         esac
#         arch="mips"
#     ;;
#     parisc*|hppa*)
#         arch="parisc"
#     ;;
#     "Power Macintosh"|ppc*|powerpc*)
#         arch="ppc"
#     ;;
#     s390|s390x)
#         arch="s390"
#     ;;
#     sh4|sh)
#         arch="sh4"
#     ;;
#     sun4*|sparc*)
#         arch="sparc"
#     ;;
#     tilegx|tile-gx)
#         arch="tilegx"
#     ;;
#     i[3-6]86*|i86pc|BePC|x86pc|x86_64|x86_32|amd64)
#         arch="x86"
#     ;;
# esac

# is_in $arch $ARCH_LIST || warn "unknown architecture $arch"
# enable $arch

# # Add processor-specific flags
# if enabled aarch64; then

#     case $cpu in
#         armv*)
#             cpuflags="-march=$cpu"
#         ;;
#         *)
#             cpuflags="-mcpu=$cpu"
#         ;;
#     esac

# elif enabled alpha; then

#     cpuflags="-mcpu=$cpu"

# elif enabled arm; then

#     check_arm_arch() {
#         test_cpp_condition stddef.h \
#             "defined __ARM_ARCH_${1}__ || defined __TARGET_ARCH_${2:-$1}" \
#             $cpuflags
#     }

#     probe_arm_arch() {
#         if   check_arm_arch 4;        then echo armv4
#         elif check_arm_arch 4T;       then echo armv4t
#         elif check_arm_arch 5;        then echo armv5
#         elif check_arm_arch 5E;       then echo armv5e
#         elif check_arm_arch 5T;       then echo armv5t
#         elif check_arm_arch 5TE;      then echo armv5te
#         elif check_arm_arch 5TEJ;     then echo armv5te
#         elif check_arm_arch 6;        then echo armv6
#         elif check_arm_arch 6J;       then echo armv6j
#         elif check_arm_arch 6K;       then echo armv6k
#         elif check_arm_arch 6Z;       then echo armv6z
#         elif check_arm_arch 6KZ;      then echo armv6zk
#         elif check_arm_arch 6ZK;      then echo armv6zk
#         elif check_arm_arch 6T2;      then echo armv6t2
#         elif check_arm_arch 7;        then echo armv7
#         elif check_arm_arch 7A  7_A;  then echo armv7-a
#         elif check_arm_arch 7S;       then echo armv7-a
#         elif check_arm_arch 7R  7_R;  then echo armv7-r
#         elif check_arm_arch 7M  7_M;  then echo armv7-m
#         elif check_arm_arch 7EM 7E_M; then echo armv7-m
#         elif check_arm_arch 8A  8_A;  then echo armv8-a
#         fi
#     }

#     [ "$cpu" = generic ] && cpu=$(probe_arm_arch)

#     case $cpu in
#         armv*)
#             cpuflags="-march=$cpu"
#             subarch=$(echo $cpu | sed 's/[^a-z0-9]//g')
#         ;;
#         *)
#             cpuflags="-mcpu=$cpu"
#             case $cpu in
#                 cortex-a*)                               subarch=armv7a  ;;
#                 cortex-r*)                               subarch=armv7r  ;;
#                 cortex-m*)                 enable thumb; subarch=armv7m  ;;
#                 arm11*)                                  subarch=armv6   ;;
#                 arm[79]*e*|arm9[24]6*|arm96*|arm102[26]) subarch=armv5te ;;
#                 armv4*|arm7*|arm9[24]*)                  subarch=armv4   ;;
#                 *)                             subarch=$(probe_arm_arch) ;;
#             esac
#         ;;
#     esac

#     case "$subarch" in
#         armv5t*)    enable fast_clz                ;;
#         armv[6-8]*)
#             enable fast_clz
#             disabled fast_unaligned || enable fast_unaligned
#             ;;
#     esac

# elif enabled avr32; then

#     case $cpu in
#         ap7[02]0[0-2])
#             subarch="avr32_ap"
#             cpuflags="-mpart=$cpu"
#         ;;
#         ap)
#             subarch="avr32_ap"
#             cpuflags="-march=$cpu"
#         ;;
#         uc3[ab]*)
#             subarch="avr32_uc"
#             cpuflags="-mcpu=$cpu"
#         ;;
#         uc)
#             subarch="avr32_uc"
#             cpuflags="-march=$cpu"
#         ;;
#     esac

# elif enabled bfin; then

#     cpuflags="-mcpu=$cpu"

# elif enabled mips; then

#     cpuflags="-march=$cpu"

#     if [ "$cpu" != "generic" ]; then
#         disable mips32r2
#         disable mips32r5
#         disable mips64r2
#         disable mips32r6
#         disable mips64r6
#         disable loongson2
#         disable loongson3

#         case $cpu in
#             24kc|24kf*|24kec|34kc|1004kc|24kef*|34kf*|1004kf*|74kc|74kf)
#                 enable mips32r2
#                 disable msa
#             ;;
#             p5600|i6400|p6600)
#                 disable mipsdsp
#                 disable mipsdspr2
#             ;;
#             loongson*)
#                 enable loongson2
#                 enable loongson3
#                 enable local_aligned
#                 enable simd_align_16
#                 enable fast_64bit
#                 enable fast_clz
#                 enable fast_cmov
#                 enable fast_unaligned
#                 disable aligned_stack
#                 disable mipsdsp
#                 disable mipsdspr2
#                 # When gcc version less than 5.3.0, add -fno-expensive-optimizations flag.
#                 if [ $cc == gcc ]; then
#                     gcc_version=$(gcc -dumpversion)
#                     if [ "$(echo "$gcc_version 5.3.0" | tr " " "\n" | sort -rV | head -n 1)" == "$gcc_version" ]; then
#                         expensive_optimization_flag=""
#                     else
#                         expensive_optimization_flag="-fno-expensive-optimizations"
#                     fi
#                 fi
#                 case $cpu in
#                     loongson3*)
#                         cpuflags="-march=loongson3a -mhard-float $expensive_optimization_flag"
#                     ;;
#                     loongson2e)
#                         cpuflags="-march=loongson2e -mhard-float $expensive_optimization_flag"
#                     ;;
#                     loongson2f)
#                         cpuflags="-march=loongson2f -mhard-float $expensive_optimization_flag"
#                     ;;
#                 esac
#             ;;
#             *)
#                 # Unknown CPU. Disable everything.
#                 warn "unknown CPU. Disabling all MIPS optimizations."
#                 disable mipsfpu
#                 disable mipsdsp
#                 disable mipsdspr2
#                 disable msa
#                 disable mmi
#             ;;
#         esac

#         case $cpu in
#             24kc)
#                 disable mipsfpu
#                 disable mipsdsp
#                 disable mipsdspr2
#             ;;
#             24kf*)
#                 disable mipsdsp
#                 disable mipsdspr2
#             ;;
#             24kec|34kc|1004kc)
#                 disable mipsfpu
#                 disable mipsdspr2
#             ;;
#             24kef*|34kf*|1004kf*)
#                 disable mipsdspr2
#             ;;
#             74kc)
#                 disable mipsfpu
#             ;;
#             p5600)
#                 enable mips32r5
#                 check_cflags "-mtune=p5600" && check_cflags "-msched-weight -mload-store-pairs -funroll-loops"
#             ;;
#             i6400)
#                 enable mips64r6
#                 check_cflags "-mtune=i6400 -mabi=64" && check_cflags "-msched-weight -mload-store-pairs -funroll-loops" && check_ldflags "-mabi=64"
#             ;;
#             p6600)
#                 enable mips64r6
#                 check_cflags "-mtune=p6600 -mabi=64" && check_cflags "-msched-weight -mload-store-pairs -funroll-loops" && check_ldflags "-mabi=64"
#             ;;
#         esac
#     else
#         # We do not disable anything. Is up to the user to disable the unwanted features.
#         warn 'generic cpu selected'
#     fi

# elif enabled ppc; then

#     disable ldbrx

#     case $(tolower $cpu) in
#         601|ppc601|powerpc601)
#             cpuflags="-mcpu=601"
#             disable altivec
#         ;;
#         603*|ppc603*|powerpc603*)
#             cpuflags="-mcpu=603"
#             disable altivec
#         ;;
#         604*|ppc604*|powerpc604*)
#             cpuflags="-mcpu=604"
#             disable altivec
#         ;;
#         g3|75*|ppc75*|powerpc75*)
#             cpuflags="-mcpu=750"
#             disable altivec
#         ;;
#         g4|745*|ppc745*|powerpc745*)
#             cpuflags="-mcpu=7450"
#             disable vsx
#         ;;
#         74*|ppc74*|powerpc74*)
#             cpuflags="-mcpu=7400"
#             disable vsx
#         ;;
#         g5|970|ppc970|powerpc970)
#             cpuflags="-mcpu=970"
#             disable vsx
#         ;;
#         power[3-6]*)
#             cpuflags="-mcpu=$cpu"
#             disable vsx
#         ;;
#         power[7-8]*)
#             cpuflags="-mcpu=$cpu"
#         ;;
#         cell)
#             cpuflags="-mcpu=cell"
#             enable ldbrx
#             disable vsx
#         ;;
#         e500mc)
#             cpuflags="-mcpu=e500mc"
#             disable altivec
#         ;;
#         e500v2)
#             cpuflags="-mcpu=8548 -mhard-float -mfloat-gprs=double"
#             disable altivec
#             disable dcbzl
#         ;;
#         e500)
#             cpuflags="-mcpu=8540 -mhard-float"
#             disable altivec
#             disable dcbzl
#         ;;
#     esac

# elif enabled sparc; then

#     case $cpu in
#         cypress|f93[04]|tsc701|sparcl*|supersparc|hypersparc|niagara|v[789])
#             cpuflags="-mcpu=$cpu"
#         ;;
#         ultrasparc*|niagara[234])
#             cpuflags="-mcpu=$cpu"
#         ;;
#     esac

# elif enabled x86; then

#     case $cpu in
#         i[345]86|pentium)
#             cpuflags="-march=$cpu"
#             disable i686
#             disable mmx
#         ;;
#         # targets that do NOT support nopl and conditional mov (cmov)
#         pentium-mmx|k6|k6-[23]|winchip-c6|winchip2|c3)
#             cpuflags="-march=$cpu"
#             disable i686
#         ;;
#         # targets that do support nopl and conditional mov (cmov)
#         i686|pentiumpro|pentium[23]|pentium-m|athlon|athlon-tbird|athlon-4|athlon-[mx]p|athlon64*|k8*|opteron*|athlon-fx\
#         |core*|atom|bonnell|nehalem|westmere|silvermont|sandybridge|ivybridge|haswell|broadwell|skylake*|knl\
#         |amdfam10|barcelona|b[dt]ver*|znver*)
#             cpuflags="-march=$cpu"
#             enable i686
#             enable fast_cmov
#         ;;
#         # targets that do support conditional mov but on which it's slow
#         pentium4|pentium4m|prescott|nocona)
#             cpuflags="-march=$cpu"
#             enable i686
#             disable fast_cmov
#         ;;
#     esac

# fi

# if [ "$cpu" != generic ]; then
#     add_cflags  $cpuflags
#     add_asflags $cpuflags
#     test "$cc_type" = "$ld_type" && add_ldflags $cpuflags
# fi

# # compiler sanity check
# test_exec <<EOF
# int main(void){ return 0; }
# EOF
# if test "$?" != 0; then
#     echo "$cc is unable to create an executable file."
#     if test -z "$cross_prefix" && ! enabled cross_compile ; then
#         echo "If $cc is a cross-compiler, use the --enable-cross-compile option."
#         echo "Only do this if you know what cross compiling means."
#     fi
#     die "C compiler test failed."
# fi

# add_cppflags -D_ISOC99_SOURCE
# add_cxxflags -D__STDC_CONSTANT_MACROS
# check_cxxflags -std=c++11 || check_cxxflags -std=c++0x

# # some compilers silently accept -std=c11, so we also need to check that the
# # version macro is defined properly
# test_cflags_cc -std=c11 ctype.h "__STDC_VERSION__ >= 201112L" &&
#     add_cflags -std=c11 ||
#     check_cflags -std=c99

# check_cppflags -D_FILE_OFFSET_BITS=64
# check_cppflags -D_LARGEFILE_SOURCE

# add_host_cppflags -D_ISOC99_SOURCE
# check_host_cflags -std=c99
# check_host_cflags -Wall
# check_host_cflags $host_cflags_speed

# check_64bit(){
#     arch32=$1
#     arch64=$2
#     expr=${3:-'sizeof(void *) > 4'}
#     test_code cc "" "int test[2*($expr) - 1]" &&
#         subarch=$arch64 || subarch=$arch32
#     enable $subarch
# }

# case "$arch" in
#     aarch64|alpha|ia64)
#         enabled shared && enable_weak pic
#     ;;
#     mips)
#         check_64bit mips mips64 '_MIPS_SIM > 1'
#         enabled shared && enable_weak pic
#     ;;
#     parisc)
#         check_64bit parisc parisc64
#         enabled shared && enable_weak pic
#     ;;
#     ppc)
#         check_64bit ppc ppc64
#         enabled shared && enable_weak pic
#     ;;
#     s390)
#         check_64bit s390 s390x
#         enabled shared && enable_weak pic
#     ;;
#     sparc)
#         check_64bit sparc sparc64
#         enabled shared && enable_weak pic
#     ;;
#     x86)
#         check_64bit x86_32 x86_64
#         # Treat x32 as x64 for now. Note it also needs pic if shared
#         test "$subarch" = "x86_32" && test_cpp_condition stddef.h 'defined(__x86_64__)' &&
#             subarch=x86_64 && enable x86_64 && disable x86_32
#         if enabled x86_64; then
#             enabled shared && enable_weak pic
#             objformat=elf64
#         fi
#     ;;
# esac

# # OS specific
# case $target_os in
#     aix)
#         SHFLAGS=-shared
#         add_cppflags '-I\$(SRC_PATH)/compat/aix'
#         enabled shared && add_ldflags -Wl,-brtl
#         arflags='-Xany -r -c'
#         striptype=""
#         ;;
#     android)
#         disable symver
#         enable section_data_rel_ro
#         add_cflags -fPIE
#         add_ldexeflags -fPIE -pie
#         SLIB_INSTALL_NAME='$(SLIBNAME)'
#         SLIB_INSTALL_LINKS=
#         SHFLAGS='-shared -Wl,-soname,$(SLIBNAME)'
#         ;;
#     haiku)
#         prefix_default="/boot/common"
#         network_extralibs="-lnetwork"
#         host_extralibs=
#         ;;
#     sunos)
#         SHFLAGS='-shared -Wl,-h,$$(@F)'
#         enabled x86 && append SHFLAGS -mimpure-text
#         network_extralibs="-lsocket -lnsl"
#         add_cppflags -D__EXTENSIONS__
#         # When using suncc to build, the Solaris linker will mark
#         # an executable with each instruction set encountered by
#         # the Solaris assembler.  As our libraries contain their own
#         # guards for processor-specific code, instead suppress
#         # generation of the HWCAPS ELF section on Solaris x86 only.
#         enabled_all suncc x86 &&
#             echo "hwcap_1 = OVERRIDE;" > mapfile &&
#             add_ldflags -Wl,-M,mapfile
#         nm_default='nm -P -g'
#         striptype=""
#         version_script='-M'
#         VERSION_SCRIPT_POSTPROCESS_CMD='perl $(SRC_PATH)/compat/solaris/make_sunver.pl - $(OBJS)'
#         ;;
#     netbsd)
#         disable symver
#         oss_indev_extralibs="-lossaudio"
#         oss_outdev_extralibs="-lossaudio"
#         enabled gcc || check_ldflags -Wl,-zmuldefs
#         ;;
#     openbsd|bitrig)
#         disable symver
#         striptype=""
#         SHFLAGS='-shared'
#         SLIB_INSTALL_NAME='$(SLIBNAME).$(LIBMAJOR).$(LIBMINOR)'
#         SLIB_INSTALL_LINKS=
#         oss_indev_extralibs="-lossaudio"
#         oss_outdev_extralibs="-lossaudio"
#         ;;
#     dragonfly)
#         disable symver
#         ;;
#     freebsd)
#         ;;
#     bsd/os)
#         add_extralibs -lpoll -lgnugetopt
#         strip="strip -d"
#         ;;
#     darwin)
#         enabled ppc && add_asflags -force_cpusubtype_ALL
#         install_name_dir_default='$(SHLIBDIR)'
#         SHFLAGS='-dynamiclib -Wl,-single_module -Wl,-install_name,$(INSTALL_NAME_DIR)/$(SLIBNAME_WITH_MAJOR),-current_version,$(LIBVERSION),-compatibility_version,$(LIBMAJOR)'
#         enabled x86_32 && append SHFLAGS -Wl,-read_only_relocs,suppress
#         strip="${strip} -x"
#         add_ldflags -Wl,-dynamic,-search_paths_first
#         check_cflags -Werror=partial-availability
#         SLIBSUF=".dylib"
#         SLIBNAME_WITH_VERSION='$(SLIBPREF)$(FULLNAME).$(LIBVERSION)$(SLIBSUF)'
#         SLIBNAME_WITH_MAJOR='$(SLIBPREF)$(FULLNAME).$(LIBMAJOR)$(SLIBSUF)'
#         enabled x86_64 && objformat="macho64" || objformat="macho32"
#         enabled_any pic shared x86_64 ||
#             { check_cflags -mdynamic-no-pic && add_asflags -mdynamic-no-pic; }
#         check_headers dispatch/dispatch.h &&
#             add_cppflags '-I\$(SRC_PATH)/compat/dispatch_semaphore'
#         if test -n "$sysroot"; then
#             is_in -isysroot $cc $CPPFLAGS $CFLAGS || check_cppflags -isysroot $sysroot
#             is_in -isysroot $ld $LDFLAGS          || check_ldflags  -isysroot $sysroot
#         fi
#         version_script='-exported_symbols_list'
#         VERSION_SCRIPT_POSTPROCESS_CMD='tr " " "\n" | sed -n /global:/,/local:/p | grep ";" | tr ";" "\n" | sed -E "s/(.+)/_\1/g" | sed -E "s/(.+[^*])$$$$/\1*/"'
#         ;;
#     msys*)
#         die "Native MSYS builds are discouraged, please use the MINGW environment."
#         ;;
#     mingw32*|mingw64*)
#         target_os=mingw32
#         LIBTARGET=i386
#         if enabled x86_64; then
#             LIBTARGET="i386:x86-64"
#         elif enabled arm; then
#             LIBTARGET="arm"
#         elif enabled aarch64; then
#             LIBTARGET="arm64"
#         fi
#         if enabled shared; then
#             # Cannot build both shared and static libs when using dllimport.
#             disable static
#         fi
#         enabled shared && ! enabled small && test_cmd $windres --version && enable gnu_windres
#         enabled x86_32 && check_ldflags -Wl,--large-address-aware
#         shlibdir_default="$bindir_default"
#         SLIBPREF=""
#         SLIBSUF=".dll"
#         SLIBNAME_WITH_VERSION='$(SLIBPREF)$(FULLNAME)-$(LIBVERSION)$(SLIBSUF)'
#         SLIBNAME_WITH_MAJOR='$(SLIBPREF)$(FULLNAME)-$(LIBMAJOR)$(SLIBSUF)'
#         if test_cmd lib.exe -list; then
#             SLIB_EXTRA_CMD=-'lib.exe -nologo -machine:$(LIBTARGET) -def:$$(@:$(SLIBSUF)=.def) -out:$(SUBDIR)$(SLIBNAME:$(SLIBSUF)=.lib)'
#             if enabled x86_64; then
#                 LIBTARGET=x64
#             fi
#         else
#             SLIB_EXTRA_CMD=-'$(DLLTOOL) -m $(LIBTARGET) -d $$(@:$(SLIBSUF)=.def) -l $(SUBDIR)$(SLIBNAME:$(SLIBSUF)=.lib) -D $(SLIBNAME_WITH_MAJOR)'
#         fi
#         SLIB_INSTALL_NAME='$(SLIBNAME_WITH_MAJOR)'
#         SLIB_INSTALL_LINKS=
#         SLIB_INSTALL_EXTRA_SHLIB='$(SLIBNAME:$(SLIBSUF)=.lib)'
#         SLIB_INSTALL_EXTRA_LIB='lib$(SLIBNAME:$(SLIBSUF)=.dll.a) $(SLIBNAME_WITH_MAJOR:$(SLIBSUF)=.def)'
#         SLIB_CREATE_DEF_CMD='EXTERN_PREFIX="$(EXTERN_PREFIX)" AR="$(AR_CMD)" NM="$(NM_CMD)" $(SRC_PATH)/compat/windows/makedef $(SUBDIR)lib$(NAME).ver $(OBJS) > $$(@:$(SLIBSUF)=.def)'
#         SHFLAGS='-shared -Wl,--out-implib,$(SUBDIR)lib$(SLIBNAME:$(SLIBSUF)=.dll.a) -Wl,--disable-auto-image-base $$(@:$(SLIBSUF)=.def)'
#         enabled x86_64 && objformat="win64" || objformat="win32"
#         dlltool="${cross_prefix}dlltool"
#         ranlib=:
#         enable dos_paths
#         check_ldflags -Wl,--nxcompat,--dynamicbase
#         # Lets work around some stupidity in binutils.
#         # ld will strip relocations from executables even though we need them
#         # for dynamicbase (ASLR).  Using -pie does retain the reloc section
#         # however ld then forgets what the entry point should be (oops) so we
#         # have to manually (re)set it.
#         if enabled x86_32; then
#             disabled debug && add_ldexeflags -Wl,--pic-executable,-e,_mainCRTStartup
#         elif enabled x86_64; then
#             disabled debug && add_ldexeflags -Wl,--pic-executable,-e,mainCRTStartup
#             check_ldflags -Wl,--high-entropy-va # binutils 2.25
#             # Set image base >4GB for extra entropy with HEASLR
#             add_ldexeflags -Wl,--image-base,0x140000000
#             append SHFLAGS -Wl,--image-base,0x180000000
#         fi
#         ;;
#     win32|win64)
#         disable symver
#         if enabled shared; then
#             # Link to the import library instead of the normal static library
#             # for shared libs.
#             LD_LIB='%.lib'
#             # Cannot build both shared and static libs with MSVC or icl.
#             disable static
#         fi
#         enabled x86_32 && check_ldflags -LARGEADDRESSAWARE
#         shlibdir_default="$bindir_default"
#         SLIBPREF=""
#         SLIBSUF=".dll"
#         SLIBNAME_WITH_VERSION='$(SLIBPREF)$(FULLNAME)-$(LIBVERSION)$(SLIBSUF)'
#         SLIBNAME_WITH_MAJOR='$(SLIBPREF)$(FULLNAME)-$(LIBMAJOR)$(SLIBSUF)'
#         SLIB_CREATE_DEF_CMD='EXTERN_PREFIX="$(EXTERN_PREFIX)" $(SRC_PATH)/compat/windows/makedef $(SUBDIR)lib$(NAME).ver $(OBJS) > $$(@:$(SLIBSUF)=.def)'
#         SLIB_INSTALL_NAME='$(SLIBNAME_WITH_MAJOR)'
#         SLIB_INSTALL_LINKS=
#         SLIB_INSTALL_EXTRA_SHLIB='$(SLIBNAME:$(SLIBSUF)=.lib)'
#         SLIB_INSTALL_EXTRA_LIB='$(SLIBNAME_WITH_MAJOR:$(SLIBSUF)=.def)'
#         SHFLAGS='-dll -def:$$(@:$(SLIBSUF)=.def) -implib:$(SUBDIR)$(SLIBNAME:$(SLIBSUF)=.lib)'
#         enabled x86_64 && objformat="win64" || objformat="win32"
#         ranlib=:
#         enable dos_paths
#         ;;
#     cygwin*)
#         target_os=cygwin
#         shlibdir_default="$bindir_default"
#         SLIBPREF="cyg"
#         SLIBSUF=".dll"
#         SLIBNAME_WITH_VERSION='$(SLIBPREF)$(FULLNAME)-$(LIBVERSION)$(SLIBSUF)'
#         SLIBNAME_WITH_MAJOR='$(SLIBPREF)$(FULLNAME)-$(LIBMAJOR)$(SLIBSUF)'
#         SLIB_INSTALL_NAME='$(SLIBNAME_WITH_MAJOR)'
#         SLIB_INSTALL_LINKS=
#         SLIB_INSTALL_EXTRA_LIB='lib$(FULLNAME).dll.a'
#         SHFLAGS='-shared -Wl,--out-implib,$(SUBDIR)lib$(FULLNAME).dll.a'
#         enabled x86_64 && objformat="win64" || objformat="win32"
#         enable dos_paths
#         enabled shared && ! enabled small && test_cmd $windres --version && enable gnu_windres
#         add_cppflags -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600
#         ;;
#     *-dos|freedos|opendos)
#         network_extralibs="-lsocket"
#         objformat="coff"
#         enable dos_paths
#         ;;
#     linux)
#         enable section_data_rel_ro
#         enabled_any arm aarch64 && enable_weak linux_perf
#         ;;
#     irix*)
#         target_os=irix
#         ranlib="echo ignoring ranlib"
#         ;;
#     os/2*)
#         strip="lxlite -CS"
#         striptype=""
#         objformat="aout"
#         add_cppflags -D_GNU_SOURCE
#         add_ldflags -Zomf -Zbin-files -Zargs-wild -Zhigh-mem -Zmap
#         SHFLAGS='$(SUBDIR)$(NAME).def -Zdll -Zomf'
#         LIBSUF="_s.a"
#         SLIBPREF=""
#         SLIBSUF=".dll"
#         SLIBNAME_WITH_VERSION='$(SLIBPREF)$(FULLNAME)-$(LIBVERSION)$(SLIBSUF)'
#         SLIBNAME_WITH_MAJOR='$(SLIBPREF)$(shell echo $(FULLNAME) | cut -c1-6)$(LIBMAJOR)$(SLIBSUF)'
#         SLIB_CREATE_DEF_CMD='echo LIBRARY $(SLIBNAME_WITH_MAJOR:$(SLIBSUF)=) INITINSTANCE TERMINSTANCE > $(SUBDIR)$(FULLNAME).def; \
#             echo CODE PRELOAD MOVEABLE DISCARDABLE >> $(SUBDIR)$(FULLNAME).def; \
#             echo DATA PRELOAD MOVEABLE MULTIPLE NONSHARED >> $(SUBDIR)$(FULLNAME).def; \
#             echo EXPORTS >> $(SUBDIR)$(FULLNAME).def; \
#             emxexp $(OBJS) >> $(SUBDIR)$(FULLNAME).def'
#         SLIB_EXTRA_CMD='emximp -o $(SUBDIR)$(LIBPREF)$(FULLNAME)_dll.a $(SUBDIR)$(FULLNAME).def; \
#             emximp -o $(SUBDIR)$(LIBPREF)$(FULLNAME)_dll.lib $(SUBDIR)$(FULLNAME).def;'
#         SLIB_INSTALL_NAME='$(SLIBNAME_WITH_MAJOR)'
#         SLIB_INSTALL_LINKS=
#         SLIB_INSTALL_EXTRA_LIB='$(LIBPREF)$(FULLNAME)_dll.a $(LIBPREF)$(FULLNAME)_dll.lib'
#         enable dos_paths
#         enable_weak os2threads
#         ;;
#     gnu/kfreebsd)
#         add_cppflags -D_BSD_SOURCE
#         ;;
#     gnu)
#         ;;
#     qnx)
#         add_cppflags -D_QNX_SOURCE
#         network_extralibs="-lsocket"
#         ;;
#     symbian)
#         SLIBSUF=".dll"
#         enable dos_paths
#         add_cflags --include=$sysinclude/gcce/gcce.h -fvisibility=default
#         add_cppflags -D__GCCE__ -D__SYMBIAN32__ -DSYMBIAN_OE_POSIX_SIGNALS
#         add_ldflags -Wl,--target1-abs,--no-undefined \
#                     -Wl,-Ttext,0x80000,-Tdata,0x1000000 -shared \
#                     -Wl,--entry=_E32Startup -Wl,-u,_E32Startup
#         add_extralibs -l:eexe.lib -l:usrt2_2.lib -l:dfpaeabi.dso \
#                       -l:drtaeabi.dso -l:scppnwdl.dso -lsupc++ -lgcc \
#                       -l:libc.dso -l:libm.dso -l:euser.dso -l:libcrt0.lib
#         ;;
#     minix)
#         ;;
#     none)
#         ;;
#     *)
#         die "Unknown OS '$target_os'."
#         ;;
# esac

# # test if creating links works
# link_dest=$(mktemp -u $TMPDIR/dest_XXXXXXXX)
# link_name=$(mktemp -u $TMPDIR/name_XXXXXXXX)
# mkdir "$link_dest"
# $ln_s "$link_dest" "$link_name"
# touch "$link_dest/test_file"
# if [ "$source_path" != "." ] && [ "$source_path" != "src" ] && ([ ! -d src ] || [ -L src ]) && [ -e "$link_name/test_file" ]; then
#     # create link to source path
#     [ -e src ] && rm src
#     $ln_s "$source_path" src
#     source_link=src
# else
#     # creating directory links doesn't work
#     # fall back to using the full source path
#     source_link="$source_path"
# fi
# # cleanup
# rm -r "$link_dest"
# rm -r "$link_name"

# # determine libc flavour

# probe_libc(){
#     pfx=$1
#     pfx_no_=${pfx%_}
#     # uclibc defines __GLIBC__, so it needs to be checked before glibc.
#     if test_${pfx}cpp_condition features.h "defined __UCLIBC__"; then
#         eval ${pfx}libc_type=uclibc
#         add_${pfx}cppflags -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600
#     elif test_${pfx}cpp_condition features.h "defined __GLIBC__"; then
#         eval ${pfx}libc_type=glibc
#         add_${pfx}cppflags -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600
#     # MinGW headers can be installed on Cygwin, so check for newlib first.
#     elif test_${pfx}cpp_condition newlib.h "defined _NEWLIB_VERSION"; then
#         eval ${pfx}libc_type=newlib
#         add_${pfx}cppflags -U__STRICT_ANSI__ -D_XOPEN_SOURCE=600
#     # MinGW64 is backwards compatible with MinGW32, so check for it first.
#     elif test_${pfx}cpp_condition _mingw.h "defined __MINGW64_VERSION_MAJOR"; then
#         eval ${pfx}libc_type=mingw64
#         if test_${pfx}cpp_condition _mingw.h "__MINGW64_VERSION_MAJOR < 3"; then
#             add_compat msvcrt/snprintf.o
#             add_cflags "-include $source_path/compat/msvcrt/snprintf.h"
#         fi
#         add_${pfx}cppflags -U__STRICT_ANSI__ -D__USE_MINGW_ANSI_STDIO=1
#         eval test \$${pfx_no_}cc_type = "gcc" &&
#             add_${pfx}cppflags -D__printf__=__gnu_printf__
#         test_${pfx}cpp_condition windows.h "!defined(_WIN32_WINNT) || _WIN32_WINNT < 0x0600" &&
#             add_${pfx}cppflags -D_WIN32_WINNT=0x0600
#         add_${pfx}cppflags -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600
#     elif test_${pfx}cpp_condition _mingw.h "defined __MINGW_VERSION"  ||
#          test_${pfx}cpp_condition _mingw.h "defined __MINGW32_VERSION"; then
#         eval ${pfx}libc_type=mingw32
#         test_${pfx}cpp_condition _mingw.h "__MINGW32_MAJOR_VERSION > 3 || \
#             (__MINGW32_MAJOR_VERSION == 3 && __MINGW32_MINOR_VERSION >= 15)" ||
#             die "ERROR: MinGW32 runtime version must be >= 3.15."
#         add_${pfx}cppflags -U__STRICT_ANSI__ -D__USE_MINGW_ANSI_STDIO=1
#         test_${pfx}cpp_condition _mingw.h "__MSVCRT_VERSION__ < 0x0700" &&
#             add_${pfx}cppflags -D__MSVCRT_VERSION__=0x0700
#         test_${pfx}cpp_condition windows.h "!defined(_WIN32_WINNT) || _WIN32_WINNT < 0x0600" &&
#             add_${pfx}cppflags -D_WIN32_WINNT=0x0600
#         eval test \$${pfx_no_}cc_type = "gcc" &&
#             add_${pfx}cppflags -D__printf__=__gnu_printf__
#         add_${pfx}cppflags -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600
#     elif test_${pfx}cpp_condition crtversion.h "defined _VC_CRT_MAJOR_VERSION"; then
#         eval ${pfx}libc_type=msvcrt
#         if test_${pfx}cpp_condition crtversion.h "_VC_CRT_MAJOR_VERSION < 14"; then
#             if [ "$pfx" = host_ ]; then
#                 add_host_cppflags -Dsnprintf=_snprintf
#             else
#                 add_compat strtod.o strtod=avpriv_strtod
#                 add_compat msvcrt/snprintf.o snprintf=avpriv_snprintf   \
#                                              _snprintf=avpriv_snprintf  \
#                                              vsnprintf=avpriv_vsnprintf
#             fi
#         fi
#         add_${pfx}cppflags -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -D_CRT_NONSTDC_NO_WARNINGS
#         # The MSVC 2010 headers (Win 7.0 SDK) set _WIN32_WINNT to
#         # 0x601 by default unless something else is set by the user.
#         # This can easily lead to us detecting functions only present
#         # in such new versions and producing binaries requiring windows 7.0.
#         # Therefore explicitly set the default to Vista unless the user has
#         # set something else on the command line.
#         # Don't do this if WINAPI_FAMILY is set and is set to a non-desktop
#         # family. For these cases, configure is free to use any functions
#         # found in the SDK headers by default. (Alternatively, we could force
#         # _WIN32_WINNT to 0x0602 in that case.)
#         test_${pfx}cpp_condition stdlib.h "defined(_WIN32_WINNT)" ||
#             { test_${pfx}cpp <<EOF && add_${pfx}cppflags -D_WIN32_WINNT=0x0600; }
# #ifdef WINAPI_FAMILY
# #include <winapifamily.h>
# #if !WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# #error not desktop
# #endif
# #endif
# EOF
#         if [ "$pfx" = "" ]; then
#             check_func strtoll || add_cflags -Dstrtoll=_strtoi64
#             check_func strtoull || add_cflags -Dstrtoull=_strtoui64
#         fi
#     elif test_${pfx}cpp_condition stddef.h "defined __KLIBC__"; then
#         eval ${pfx}libc_type=klibc
#     elif test_${pfx}cpp_condition sys/cdefs.h "defined __BIONIC__"; then
#         eval ${pfx}libc_type=bionic
#     elif test_${pfx}cpp_condition sys/brand.h "defined LABELED_BRAND_NAME"; then
#         eval ${pfx}libc_type=solaris
#         add_${pfx}cppflags -D__EXTENSIONS__ -D_XOPEN_SOURCE=600
#     elif test_${pfx}cpp_condition sys/version.h "defined __DJGPP__"; then
#         eval ${pfx}libc_type=djgpp
#         add_cppflags -U__STRICT_ANSI__
#         add_cflags "-include $source_path/compat/djgpp/math.h"
#         add_compat djgpp/math.o
#     fi
#     test_${pfx}cc <<EOF
# #include <time.h>
# void *v = localtime_r;
# EOF
# test "$?" != 0 && test_${pfx}cc -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600 <<EOF && add_${pfx}cppflags -D_POSIX_C_SOURCE=200112 -D_XOPEN_SOURCE=600
# #include <time.h>
# void *v = localtime_r;
# EOF

#     eval test -n "\${${pfx}libc_type}" && enable ${pfx}libc_${libc_type}
# }

# probe_libc
# probe_libc host_

# # hacks for compiler/libc/os combinations

# case $libc_type in
#     bionic)
#         add_compat strtod.o strtod=avpriv_strtod
#         ;;
# esac

# check_compile_assert flt_lim "float.h limits.h" "DBL_MAX == (double)DBL_MAX" ||
#     add_cppflags '-I\$(SRC_PATH)/compat/float'

# test_cpp_condition stdlib.h "defined(__PIC__) || defined(__pic__) || defined(PIC)" && enable_weak pic

# set_default libdir
# : ${shlibdir_default:="$libdir"}
# : ${pkgconfigdir_default:="$libdir/pkgconfig"}

# set_default $PATHS_LIST
# set_default nm

# disabled optimizations || enabled ossfuzz || check_cflags -fomit-frame-pointer

# enable_weak_pic() {
#     disabled pic && return
#     enable pic
#     add_cppflags -DPIC
#     case "$target_os" in
#     mingw*|cygwin*|win*)
#         ;;
#     *)
#         add_cflags -fPIC
#         add_asflags -fPIC
#         ;;
#     esac
# }

# enabled pic && enable_weak_pic

# test_cc <<EOF || die "Symbol mangling check failed."
# int ff_extern;
# EOF
# sym=$($nm $TMPO | awk '/ff_extern/{ print substr($0, match($0, /[^ \t]*ff_extern/)) }')
# extern_prefix=${sym%%ff_extern*}

# ! disabled inline_asm && check_inline_asm inline_asm '"" ::'

# for restrict_keyword in restrict __restrict__ __restrict ""; do
#     test_code cc "" "char * $restrict_keyword p" && break
# done

# check_cc pragma_deprecated "" '_Pragma("GCC diagnostic ignored \"-Wdeprecated-declarations\"")'

# # The global variable ensures the bits appear unchanged in the object file.
# test_cc <<EOF || die "endian test failed"
# unsigned int endian = 'B' << 24 | 'I' << 16 | 'G' << 8 | 'E';
# EOF
# od -t x1 $TMPO | grep -q '42 *49 *47 *45' && enable bigendian

# check_cc const_nan math.h "struct { double d; } static const bar[] = { { NAN } }"

# if ! enabled ppc64 || enabled bigendian; then
#     disable vsx
# fi

# check_gas() {
#     log "check_gas using '$as' as AS"
#     # :vararg is used on aarch64, arm and ppc altivec
#     check_as vararg "
# .macro m n, y:vararg=0
# \n: .int \y
# .endm
# m x" || return 1
#     # .altmacro is only used in arm asm
#     ! enabled arm || check_as gnu_as ".altmacro"
# }

# if enabled_any arm aarch64 || enabled_all ppc altivec && enabled asm; then
#     nogas=:
#     enabled_any arm aarch64 && nogas=die
#     enabled_all ppc altivec && [ $target_os_default != aix ] && nogas=warn
#     as_noop=-v

#     case $as_type in
#         arm*) gaspp_as_type=armasm; as_noop=-h ;;
#         gcc)  gaspp_as_type=gas ;;
#         *)    gaspp_as_type=$as_type ;;
#     esac

#     [ $target_os = "darwin" ] && gaspp_as_type="apple-$gaspp_as_type"

#     test "${as#*gas-preprocessor.pl}" != "$as" ||
#     test_cmd gas-preprocessor.pl -arch $arch -as-type $gaspp_as_type -- ${as:=$cc} $as_noop &&
#         gas="${gas:=gas-preprocessor.pl} -arch $arch -as-type $gaspp_as_type -- ${as:=$cc}"

#     if ! check_gas ; then
#         as=${gas:=$as}
#         check_gas || \
#             $nogas "GNU assembler not found, install/update gas-preprocessor"
#     fi

#     check_as as_func ".func test
#                       .endfunc"
# fi

# check_inline_asm inline_asm_labels '"1:\n"'

# check_inline_asm inline_asm_nonlocal_labels '"Label:\n"'

# if enabled aarch64; then
#     enabled armv8 && check_insn armv8 'prfm   pldl1strm, [x0]'
#     # internal assembler in clang 3.3 does not support this instruction
#     enabled neon && check_insn neon 'ext   v0.8B, v0.8B, v1.8B, #1'
#     enabled vfp  && check_insn vfp  'fmadd d0,    d0,    d1,    d2'

#     map 'enabled_any ${v}_external ${v}_inline || disable $v' $ARCH_EXT_LIST_ARM

# elif enabled alpha; then

#     check_cflags -mieee

# elif enabled arm; then

#     enabled msvc && check_cpp_condition thumb stddef.h "defined _M_ARMT"
#     test_cpp_condition stddef.h "defined __thumb__" && test_cc <<EOF && enable_weak thumb
# float func(float a, float b){ return a+b; }
# EOF
#     enabled thumb && check_cflags -mthumb || check_cflags -marm

#     if check_cpp_condition vfp_args stddef.h "defined __ARM_PCS_VFP"; then
#         :
#     elif check_cpp_condition vfp_args stddef.h "defined _M_ARM_FP && _M_ARM_FP >= 30"; then
#         :
#     elif ! test_cpp_condition stddef.h "defined __ARM_PCS || defined __SOFTFP__" && [ $target_os != darwin ]; then
#         case "${cross_prefix:-$cc}" in
#             *hardfloat*) enable vfp_args; fpabi=vfp ;;
#             *) check_ld "cc" vfp_args <<EOF && fpabi=vfp || fpabi=soft ;;
# __asm__ (".eabi_attribute 28, 1");
# int main(void) { return 0; }
# EOF
#         esac
#         warn "Compiler does not indicate floating-point ABI, guessing $fpabi."
#     fi

#     enabled armv5te && check_insn armv5te 'qadd r0, r0, r0'
#     enabled armv6   && check_insn armv6   'sadd16 r0, r0, r0'
#     enabled armv6t2 && check_insn armv6t2 'movt r0, #0'
#     enabled neon    && check_insn neon    'vadd.i16 q0, q0, q0'
#     enabled vfp     && check_insn vfp     'fadds s0, s0, s0'
#     enabled vfpv3   && check_insn vfpv3   'vmov.f32 s0, #1.0'
#     enabled setend  && check_insn setend  'setend be'

#     [ $target_os = linux ] || [ $target_os = android ] ||
#         map 'enabled_any ${v}_external ${v}_inline || disable $v' \
#             $ARCH_EXT_LIST_ARM

#     check_inline_asm asm_mod_q '"add r0, %Q0, %R0" :: "r"((long long)0)'

#     check_as as_arch_directive ".arch armv7-a"
#     check_as as_dn_directive   "ra .dn d0.i16"
#     check_as as_fpu_directive  ".fpu neon"

#     # llvm's integrated assembler supports .object_arch from llvm 3.5
#     [ "$objformat" = elf32 ] || [ "$objformat" = elf64 ] &&
#         check_as as_object_arch ".object_arch armv4"

#     # MS armasm fails to assemble our PIC constructs
#     [ $target_os != win32 ] && enabled_all armv6t2 shared !pic && enable_weak_pic

# elif enabled mips; then

#     enabled loongson2 && check_inline_asm loongson2 '"dmult.g $8, $9, $10"'
#     enabled loongson3 && check_inline_asm loongson3 '"gsldxc1 $f0, 0($2, $3)"'
#     enabled mmi && check_inline_asm mmi '"punpcklhw $f0, $f0, $f0"'

#     # Enable minimum ISA based on selected options
#     if enabled mips64; then
#         enabled mips64r6 && check_inline_asm_flags mips64r6 '"dlsa $0, $0, $0, 1"' '-mips64r6'
#         enabled mips64r2 && check_inline_asm_flags mips64r2 '"dext $0, $0, 0, 1"' '-mips64r2'
#         disabled mips64r6 && disabled mips64r2 && check_inline_asm_flags mips64r1 '"daddi $0, $0, 0"' '-mips64'
#     else
#         enabled mips32r6 && check_inline_asm_flags mips32r6 '"aui $0, $0, 0"' '-mips32r6'
#         enabled mips32r5 && check_inline_asm_flags mips32r5 '"eretnc"' '-mips32r5'
#         enabled mips32r2 && check_inline_asm_flags mips32r2 '"ext $0, $0, 0, 1"' '-mips32r2'
#         disabled mips32r6 && disabled mips32r5 && disabled mips32r2 && check_inline_asm_flags mips32r1 '"addi $0, $0, 0"' '-mips32'
#     fi

#     enabled mipsfpu && check_inline_asm_flags mipsfpu '"cvt.d.l $f0, $f2"' '-mhard-float'
#     enabled mipsfpu && (enabled mips32r5 || enabled mips32r6 || enabled mips64r6) && check_inline_asm_flags mipsfpu '"cvt.d.l $f0, $f1"' '-mfp64'
#     enabled mipsfpu && enabled msa && check_inline_asm_flags msa '"addvi.b $w0, $w1, 1"' '-mmsa' && check_headers msa.h || disable msa
#     enabled mipsdsp && check_inline_asm_flags mipsdsp '"addu.qb $t0, $t1, $t2"' '-mdsp'
#     enabled mipsdspr2 && check_inline_asm_flags mipsdspr2 '"absq_s.qb $t0, $t1"' '-mdspr2'
#     enabled msa && enabled msa2 && check_inline_asm_flags msa2 '"nxbits.any.b $w0, $w0"' '-mmsa2' && check_headers msa2.h || disable msa2

#     if enabled bigendian && enabled msa; then
#         disable msa
#     fi

# elif enabled parisc; then

#     if enabled gcc; then
#         case $($cc -dumpversion) in
#             4.[3-9].*) check_cflags -fno-optimize-sibling-calls ;;
#         esac
#     fi

# elif enabled ppc; then

#     enable local_aligned

#     check_inline_asm dcbzl     '"dcbzl 0, %0" :: "r"(0)'
#     check_inline_asm ibm_asm   '"add 0, 0, 0"'
#     check_inline_asm ppc4xx    '"maclhw r10, r11, r12"'
#     check_inline_asm xform_asm '"lwzx %1, %y0" :: "Z"(*(int*)0), "r"(0)'

#     if enabled altivec; then
#         check_cflags -maltivec -mabi=altivec

#         # check if our compiler supports Motorola AltiVec C API
#         check_cc altivec altivec.h "vector signed int v1 = (vector signed int) { 0 };
#                                     vector signed int v2 = (vector signed int) { 1 };
#                                     v1 = vec_add(v1, v2);"

#         enabled altivec || warn "Altivec disabled, possibly missing --cpu flag"
#     fi

#     if enabled vsx; then
#         check_cflags -mvsx &&
#         check_cc vsx altivec.h "int v[4] = { 0 };
#                                 vector signed int v1 = vec_vsx_ld(0, v);"
#     fi

#     if enabled power8; then
#         check_cpp_condition power8 "altivec.h" "defined(_ARCH_PWR8)"
#     fi

# elif enabled x86; then

#     check_builtin rdtsc    intrin.h   "__rdtsc()"
#     check_builtin mm_empty mmintrin.h "_mm_empty()"

#     enable local_aligned

#     # check whether EBP is available on x86
#     # As 'i' is stored on the stack, this program will crash
#     # if the base pointer is used to access it because the
#     # base pointer is cleared in the inline assembly code.
#     check_exec_crash <<EOF && enable ebp_available
# volatile int i=0;
# __asm__ volatile ("xorl %%ebp, %%ebp" ::: "%ebp");
# return i;
# EOF

#     # check whether EBX is available on x86
#     check_inline_asm ebx_available '""::"b"(0)' &&
#         check_inline_asm ebx_available '"":::"%ebx"'

#     # check whether xmm clobbers are supported
#     check_inline_asm xmm_clobbers '"":::"%xmm0"'

#     check_inline_asm inline_asm_direct_symbol_refs '"movl '$extern_prefix'test, %eax"' ||
#         check_inline_asm inline_asm_direct_symbol_refs '"movl '$extern_prefix'test(%rip), %eax"'

#     # check whether binutils is new enough to compile SSSE3/MMXEXT
#     enabled ssse3  && check_inline_asm ssse3_inline  '"pabsw %xmm0, %xmm0"'
#     enabled mmxext && check_inline_asm mmxext_inline '"pmaxub %mm0, %mm1"'

#     probe_x86asm(){
#         x86asmexe_probe=$1
#         if test_cmd $x86asmexe_probe -v; then
#             x86asmexe=$x86asmexe_probe
#             x86asm_type=nasm
#             x86asm_debug="-g -F dwarf"
#             X86ASMDEP=
#             X86ASM_DEPFLAGS='-MD $(@:.o=.d)'
#         elif test_cmd $x86asmexe_probe --version; then
#             x86asmexe=$x86asmexe_probe
#             x86asm_type=yasm
#             x86asm_debug="-g dwarf2"
#             X86ASMDEP='$(DEPX86ASM) $(X86ASMFLAGS) -M $(X86ASM_O) $< > $(@:.o=.d)'
#             X86ASM_DEPFLAGS=
#         fi
#         check_x86asm x86asm "movbe ecx, [5]"
#     }

#     if ! disabled_any asm mmx x86asm; then
#         disable x86asm
#         for program in $x86asmexe nasm yasm; do
#             probe_x86asm $program && break
#         done
#         disabled x86asm && die "nasm/yasm not found or too old. Use --disable-x86asm for a crippled build."
#         X86ASMFLAGS="-f $objformat"
#         enabled pic               && append X86ASMFLAGS "-DPIC"
#         test -n "$extern_prefix"  && append X86ASMFLAGS "-DPREFIX"
#         case "$objformat" in
#             elf*) enabled debug && append X86ASMFLAGS $x86asm_debug ;;
#         esac

#         check_x86asm avx512_external "vmovdqa32 [eax]{k1}{z}, zmm0"
#         check_x86asm avx2_external   "vextracti128 xmm0, ymm0, 0"
#         check_x86asm xop_external    "vpmacsdd xmm0, xmm1, xmm2, xmm3"
#         check_x86asm fma4_external   "vfmaddps ymm0, ymm1, ymm2, ymm3"
#         check_x86asm cpunop          "CPU amdnop"
#     fi

#     case "$cpu" in
#         athlon*|opteron*|k8*|pentium|pentium-mmx|prescott|nocona|atom|geode)
#             disable fast_clz
#         ;;
#     esac

# fi

# check_cc intrinsics_neon arm_neon.h "int16x8_t test = vdupq_n_s16(0)"

# check_ldflags -Wl,--as-needed
# check_ldflags -Wl,-z,noexecstack

# if ! disabled network; then
#     check_func getaddrinfo $network_extralibs
#     check_func inet_aton $network_extralibs

#     check_type netdb.h "struct addrinfo"
#     check_type netinet/in.h "struct group_source_req" -D_BSD_SOURCE
#     check_type netinet/in.h "struct ip_mreq_source" -D_BSD_SOURCE
#     check_type netinet/in.h "struct ipv6_mreq" -D_DARWIN_C_SOURCE
#     check_type poll.h "struct pollfd"
#     check_type netinet/sctp.h "struct sctp_event_subscribe"
#     check_struct "sys/socket.h" "struct msghdr" msg_flags
#     check_struct "sys/types.h sys/socket.h" "struct sockaddr" sa_len
#     check_type netinet/in.h "struct sockaddr_in6"
#     check_type "sys/types.h sys/socket.h" "struct sockaddr_storage"
#     check_type "sys/types.h sys/socket.h" socklen_t

#     # Prefer arpa/inet.h over winsock2
#     if check_headers arpa/inet.h ; then
#         check_func closesocket
#     elif check_headers winsock2.h ; then
#         check_func_headers winsock2.h closesocket -lws2 &&
#             network_extralibs="-lws2" ||
#         { check_func_headers winsock2.h closesocket -lws2_32 &&
#             network_extralibs="-lws2_32"; } || disable winsock2_h network
#         check_func_headers ws2tcpip.h getaddrinfo $network_extralibs

#         check_type ws2tcpip.h socklen_t
#         check_type ws2tcpip.h "struct addrinfo"
#         check_type ws2tcpip.h "struct group_source_req"
#         check_type ws2tcpip.h "struct ip_mreq_source"
#         check_type ws2tcpip.h "struct ipv6_mreq"
#         check_type winsock2.h "struct pollfd"
#         check_struct winsock2.h "struct sockaddr" sa_len
#         check_type ws2tcpip.h "struct sockaddr_in6"
#         check_type ws2tcpip.h "struct sockaddr_storage"
#     else
#         disable network
#     fi
# fi

# check_builtin atomic_cas_ptr atomic.h "void **ptr; void *oldval, *newval; atomic_cas_ptr(ptr, oldval, newval)"
# check_builtin machine_rw_barrier mbarrier.h "__machine_rw_barrier()"
# check_builtin MemoryBarrier windows.h "MemoryBarrier()"
# check_builtin sync_val_compare_and_swap "" "int *ptr; int oldval, newval; __sync_val_compare_and_swap(ptr, oldval, newval)"
# check_builtin gmtime_r time.h "time_t *time; struct tm *tm; gmtime_r(time, tm)"
# check_builtin localtime_r time.h "time_t *time; struct tm *tm; localtime_r(time, tm)"
# check_builtin x264_csp_bgr "stdint.h x264.h" "X264_CSP_BGR"

# case "$custom_allocator" in
#     jemalloc)
#         # jemalloc by default does not use a prefix
#         require libjemalloc jemalloc/jemalloc.h malloc -ljemalloc
#     ;;
#     tcmalloc)
#         require_pkg_config libtcmalloc libtcmalloc gperftools/tcmalloc.h tc_malloc
#         malloc_prefix=tc_
#     ;;
# esac

# check_func_headers malloc.h _aligned_malloc     && enable aligned_malloc
# check_func  ${malloc_prefix}memalign            && enable memalign
# check_func  ${malloc_prefix}posix_memalign      && enable posix_memalign

# check_func  access
# check_func_headers stdlib.h arc4random
# check_lib   clock_gettime time.h clock_gettime || check_lib clock_gettime time.h clock_gettime -lrt
# check_func  fcntl
# check_func  fork
# check_func  gethrtime
# check_func  getopt
# check_func  getrusage
# check_func  gettimeofday
# check_func  isatty
# check_func  mkstemp
# check_func  mmap
# check_func  mprotect
# # Solaris has nanosleep in -lrt, OpenSolaris no longer needs that
# check_func_headers time.h nanosleep || check_lib nanosleep time.h nanosleep -lrt
# check_func  sched_getaffinity
# check_func  setrlimit
# check_struct "sys/stat.h" "struct stat" st_mtim.tv_nsec -D_BSD_SOURCE
# check_func  strerror_r
# check_func  sysconf
# check_func  sysctl
# check_func  usleep

# check_func_headers conio.h kbhit
# check_func_headers io.h setmode
# check_func_headers lzo/lzo1x.h lzo1x_999_compress
# check_func_headers mach/mach_time.h mach_absolute_time
# check_func_headers stdlib.h getenv
# check_func_headers sys/stat.h lstat

# check_func_headers windows.h GetProcessAffinityMask
# check_func_headers windows.h GetProcessTimes
# check_func_headers windows.h GetSystemTimeAsFileTime
# check_func_headers windows.h LoadLibrary
# check_func_headers windows.h MapViewOfFile
# check_func_headers windows.h PeekNamedPipe
# check_func_headers windows.h SetConsoleTextAttribute
# check_func_headers windows.h SetConsoleCtrlHandler
# check_func_headers windows.h Sleep
# check_func_headers windows.h VirtualAlloc
# check_func_headers glob.h glob
# enabled xlib &&
#     check_lib xlib "X11/Xlib.h X11/extensions/Xvlib.h" XvGetPortAttribute -lXv -lX11 -lXext

# check_headers direct.h
# check_headers dirent.h
# check_headers dxgidebug.h
# check_headers dxva.h
# check_headers dxva2api.h -D_WIN32_WINNT=0x0600
# check_headers io.h
# check_headers linux/perf_event.h
# check_headers libcrystalhd/libcrystalhd_if.h
# check_headers malloc.h
# check_headers net/udplite.h
# check_headers poll.h
# check_headers sys/param.h
# check_headers sys/resource.h
# check_headers sys/select.h
# check_headers sys/time.h
# check_headers sys/un.h
# check_headers termios.h
# check_headers unistd.h
# check_headers valgrind/valgrind.h
# check_func_headers VideoToolbox/VTCompressionSession.h VTCompressionSessionPrepareToEncodeFrames -framework VideoToolbox
# check_headers windows.h
# check_headers X11/extensions/XvMClib.h
# check_headers asm/types.h

# # it seems there are versions of clang in some distros that try to use the
# # gcc headers, which explodes for stdatomic
# # so we also check that atomics actually work here
# check_builtin stdatomic stdatomic.h "atomic_int foo, bar = ATOMIC_VAR_INIT(-1); atomic_store(&foo, 0); foo += bar"

# check_lib advapi32 "windows.h"            RegCloseKey          -ladvapi32
# check_lib bcrypt   "windows.h bcrypt.h"   BCryptGenRandom      -lbcrypt &&
#     check_cpp_condition bcrypt bcrypt.h "defined BCRYPT_RNG_ALGORITHM"
# check_lib ole32    "windows.h"            CoTaskMemFree        -lole32
# check_lib shell32  "windows.h shellapi.h" CommandLineToArgvW   -lshell32
# check_lib psapi    "windows.h psapi.h"    GetProcessMemoryInfo -lpsapi

# check_lib android android/native_window.h ANativeWindow_acquire -landroid
# check_lib mediandk "stdint.h media/NdkImage.h" AImage_delete -lmediandk
# check_lib camera2ndk "stdbool.h stdint.h camera/NdkCameraManager.h" ACameraManager_create -lcamera2ndk

# enabled appkit       && check_apple_framework AppKit
# enabled audiotoolbox && check_apple_framework AudioToolbox
# enabled avfoundation && check_apple_framework AVFoundation
# enabled coreimage    && check_apple_framework CoreImage
# enabled videotoolbox && check_apple_framework VideoToolbox

# check_apple_framework CoreFoundation
# check_apple_framework CoreMedia
# check_apple_framework CoreVideo

# enabled avfoundation && {
#     disable coregraphics applicationservices
#     check_lib coregraphics        CoreGraphics/CoreGraphics.h               CGGetActiveDisplayList "-framework CoreGraphics" ||
#     check_lib applicationservices ApplicationServices/ApplicationServices.h CGGetActiveDisplayList "-framework ApplicationServices"; }

# enabled videotoolbox && {
#     check_lib coreservices CoreServices/CoreServices.h UTGetOSTypeFromString "-framework CoreServices"
#     check_func_headers CoreMedia/CMFormatDescription.h kCMVideoCodecType_HEVC "-framework CoreMedia"
#     check_func_headers CoreVideo/CVPixelBuffer.h kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange "-framework CoreVideo"
#     check_func_headers CoreVideo/CVImageBuffer.h kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ "-framework CoreVideo"
#     check_func_headers CoreVideo/CVImageBuffer.h kCVImageBufferTransferFunction_ITU_R_2100_HLG "-framework CoreVideo"
#     check_func_headers CoreVideo/CVImageBuffer.h kCVImageBufferTransferFunction_Linear "-framework CoreVideo"
# }

# check_struct "sys/time.h sys/resource.h" "struct rusage" ru_maxrss

# check_type "windows.h dxva.h" "DXVA_PicParams_HEVC" -DWINAPI_FAMILY=WINAPI_FAMILY_DESKTOP_APP -D_CRT_BUILD_DESKTOP_APP=0
# check_type "windows.h dxva.h" "DXVA_PicParams_VP9" -DWINAPI_FAMILY=WINAPI_FAMILY_DESKTOP_APP -D_CRT_BUILD_DESKTOP_APP=0
# check_type "windows.h d3d11.h" "ID3D11VideoDecoder"
# check_type "windows.h d3d11.h" "ID3D11VideoContext"
# check_type "d3d9.h dxva2api.h" DXVA2_ConfigPictureDecode -D_WIN32_WINNT=0x0602

# check_type "vdpau/vdpau.h" "VdpPictureInfoHEVC"

# if [ -z "$nvccflags" ]; then
#     nvccflags=$nvccflags_default
# fi

# if enabled x86_64 || enabled ppc64 || enabled aarch64; then
#     nvccflags="$nvccflags -m64"
# else
#     nvccflags="$nvccflags -m32"
# fi

# if enabled cuda_nvcc; then
#     nvccflags="$nvccflags -ptx"
# else
#     nvccflags="$nvccflags -S -nocudalib -nocudainc --cuda-device-only -include ${source_link}/compat/cuda/cuda_runtime.h"
#     check_nvcc cuda_llvm
# fi

# if ! disabled ffnvcodec; then
#     ffnv_hdr_list="ffnvcodec/nvEncodeAPI.h ffnvcodec/dynlink_cuda.h ffnvcodec/dynlink_cuviddec.h ffnvcodec/dynlink_nvcuvid.h"
#     check_pkg_config ffnvcodec "ffnvcodec >= 9.0.18.0" "$ffnv_hdr_list" "" || \
#       check_pkg_config ffnvcodec "ffnvcodec >= 8.2.15.8 ffnvcodec < 8.3" "$ffnv_hdr_list" "" || \
#       check_pkg_config ffnvcodec "ffnvcodec >= 8.1.24.9 ffnvcodec < 8.2" "$ffnv_hdr_list" "" || \
#       check_pkg_config ffnvcodec "ffnvcodec >= 8.0.14.9 ffnvcodec < 8.1" "$ffnv_hdr_list" ""
# fi

# check_cpp_condition winrt windows.h "!WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)"

# if ! disabled w32threads && ! enabled pthreads; then
#     check_func_headers "windows.h process.h" _beginthreadex &&
#         check_type "windows.h" CONDITION_VARIABLE &&
#         check_type "windows.h" INIT_ONCE &&
#         enable w32threads || disable w32threads
#     if ! enabled w32threads && enabled winrt; then
#         check_func_headers "windows.h" CreateThread &&
#             enable w32threads || disable w32threads
#     fi
# fi

# # check for some common methods of building with pthread support
# # do this before the optional library checks as some of them require pthreads
# if ! disabled pthreads && ! enabled w32threads && ! enabled os2threads; then
#     if check_lib pthreads pthread.h pthread_join   -pthread &&
#        check_lib pthreads pthread.h pthread_create -pthread; then
#         add_cflags -pthread
#     elif check_lib pthreads pthread.h pthread_join   -pthreads &&
#          check_lib pthreads pthread.h pthread_create -pthreads; then
#         add_cflags -pthreads
#     elif check_lib pthreads pthread.h pthread_join   -ldl -pthread &&
#          check_lib pthreads pthread.h pthread_create -ldl -pthread; then
#         add_cflags -ldl -pthread
#     elif check_lib pthreads pthread.h pthread_join   -lpthreadGC2 &&
#          check_lib pthreads pthread.h pthread_create -lpthreadGC2; then
#         :
#     elif check_lib pthreads pthread.h pthread_join   -lpthread &&
#          check_lib pthreads pthread.h pthread_create -lpthread; then
#         :
#     elif check_func pthread_join && check_func pthread_create; then
#         enable pthreads
#     fi
#     check_cc pthreads "pthread.h" "static pthread_mutex_t atomic_lock = PTHREAD_MUTEX_INITIALIZER"

#     if enabled pthreads; then
#         check_builtin sem_timedwait semaphore.h "sem_t *s; sem_init(s,0,0); sem_timedwait(s,0); sem_destroy(s)" $pthreads_extralibs
#         check_func pthread_cancel $pthreads_extralibs
#     fi
# fi

# enabled  zlib && { check_pkg_config zlib zlib "zlib.h" zlibVersion ||
#                    check_lib zlib   zlib.h      zlibVersion    -lz; }
# enabled bzlib && check_lib bzlib bzlib.h BZ2_bzlibVersion    -lbz2
# enabled  lzma && check_lib lzma   lzma.h lzma_version_number -llzma

# # On some systems dynamic loading requires no extra linker flags
# check_lib libdl dlfcn.h "dlopen dlsym" || check_lib libdl dlfcn.h "dlopen dlsym" -ldl

# check_lib libm math.h sin -lm

# atan2f_args=2
# copysign_args=2
# hypot_args=2
# ldexpf_args=2
# powf_args=2

# for func in $MATH_FUNCS; do
#     eval check_mathfunc $func \${${func}_args:-1} $libm_extralibs
# done

# for func in $COMPLEX_FUNCS; do
#     eval check_complexfunc $func \${${func}_args:-1}
# done

# # these are off by default, so fail if requested and not available
# enabled cuda_nvcc         && { check_nvcc cuda_nvcc || die "ERROR: failed checking for nvcc."; }
# enabled chromaprint       && require chromaprint chromaprint.h chromaprint_get_version -lchromaprint
# enabled decklink          && { require_headers DeckLinkAPI.h &&
#                                { test_cpp_condition DeckLinkAPIVersion.h "BLACKMAGIC_DECKLINK_API_VERSION >= 0x0a090500" || die "ERROR: Decklink API version must be >= 10.9.5."; } }
# enabled frei0r            && require_headers "frei0r.h dlfcn.h"
# enabled gmp               && require gmp gmp.h mpz_export -lgmp
# enabled gnutls            && require_pkg_config gnutls gnutls gnutls/gnutls.h gnutls_global_init
# enabled jni               && { [ $target_os = "android" ] && check_headers jni.h && enabled pthreads || die "ERROR: jni not found"; }
# enabled ladspa            && require_headers "ladspa.h dlfcn.h"
# enabled libaom            && require_pkg_config libaom "aom >= 1.0.0" aom/aom_codec.h aom_codec_version
# enabled libaribb24        && { check_pkg_config libaribb24 "aribb24 > 1.0.3" "aribb24/aribb24.h" arib_instance_new ||
#                                { enabled gpl && require_pkg_config libaribb24 aribb24 "aribb24/aribb24.h" arib_instance_new; } ||
#                                die "ERROR: libaribb24 requires version higher than 1.0.3 or --enable-gpl."; }
# enabled lv2               && require_pkg_config lv2 lilv-0 "lilv/lilv.h" lilv_world_new
# enabled libiec61883       && require libiec61883 libiec61883/iec61883.h iec61883_cmp_connect -lraw1394 -lavc1394 -lrom1394 -liec61883
# enabled libass            && require_pkg_config libass libass ass/ass.h ass_library_init
# enabled libbluray         && require_pkg_config libbluray libbluray libbluray/bluray.h bd_open
# enabled libbs2b           && require_pkg_config libbs2b libbs2b bs2b.h bs2b_open
# enabled libcelt           && require libcelt celt/celt.h celt_decode -lcelt0 &&
#                              { check_lib libcelt celt/celt.h celt_decoder_create_custom -lcelt0 ||
#                                die "ERROR: libcelt must be installed and version must be >= 0.11.0."; }
# enabled libcaca           && require_pkg_config libcaca caca caca.h caca_create_canvas
# enabled libcodec2         && require libcodec2 codec2/codec2.h codec2_create -lcodec2
# enabled libdav1d          && require_pkg_config libdav1d "dav1d >= 0.2.1" "dav1d/dav1d.h" dav1d_version
# enabled libdavs2          && require_pkg_config libdavs2 "davs2 >= 1.6.0" davs2.h davs2_decoder_open
# enabled libdc1394         && require_pkg_config libdc1394 libdc1394-2 dc1394/dc1394.h dc1394_new
# enabled libdrm            && require_pkg_config libdrm libdrm xf86drm.h drmGetVersion
# enabled libfdk_aac        && { check_pkg_config libfdk_aac fdk-aac "fdk-aac/aacenc_lib.h" aacEncOpen ||
#                                { require libfdk_aac fdk-aac/aacenc_lib.h aacEncOpen -lfdk-aac &&
#                                  warn "using libfdk without pkg-config"; } }
# flite_extralibs="-lflite_cmu_time_awb -lflite_cmu_us_awb -lflite_cmu_us_kal -lflite_cmu_us_kal16 -lflite_cmu_us_rms -lflite_cmu_us_slt -lflite_usenglish -lflite_cmulex -lflite"
# enabled libflite          && require libflite "flite/flite.h" flite_init $flite_extralibs
# enabled fontconfig        && enable libfontconfig
# enabled libfontconfig     && require_pkg_config libfontconfig fontconfig "fontconfig/fontconfig.h" FcInit
# enabled libfreetype       && require_pkg_config libfreetype freetype2 "ft2build.h FT_FREETYPE_H" FT_Init_FreeType
# enabled libfribidi        && require_pkg_config libfribidi fribidi fribidi.h fribidi_version_info
# enabled libgme            && { check_pkg_config libgme libgme gme/gme.h gme_new_emu ||
#                                require libgme gme/gme.h gme_new_emu -lgme -lstdc++; }
# enabled libgsm            && { for gsm_hdr in "gsm.h" "gsm/gsm.h"; do
#                                    check_lib libgsm "${gsm_hdr}" gsm_create -lgsm && break;
#                                done || die "ERROR: libgsm not found"; }
# enabled libilbc           && require libilbc ilbc.h WebRtcIlbcfix_InitDecode -lilbc $pthreads_extralibs
# enabled libklvanc         && require libklvanc libklvanc/vanc.h klvanc_context_create -lklvanc
# enabled libkvazaar        && require_pkg_config libkvazaar "kvazaar >= 0.8.1" kvazaar.h kvz_api_get
# enabled liblensfun        && require_pkg_config liblensfun lensfun lensfun.h lf_db_new
# # While it may appear that require is being used as a pkg-config
# # fallback for libmfx, it is actually being used to detect a different
# # installation route altogether.  If libmfx is installed via the Intel
# # Media SDK or Intel Media Server Studio, these don't come with
# # pkg-config support.  Instead, users should make sure that the build
# # can find the libraries and headers through other means.
# enabled libmfx            && { check_pkg_config libmfx libmfx "mfx/mfxvideo.h" MFXInit ||
#                                { require libmfx "mfx/mfxvideo.h" MFXInit "-llibmfx $advapi32_extralibs" && warn "using libmfx without pkg-config"; } }
# enabled libmodplug        && require_pkg_config libmodplug libmodplug libmodplug/modplug.h ModPlug_Load
# enabled libmp3lame        && require "libmp3lame >= 3.98.3" lame/lame.h lame_set_VBR_quality -lmp3lame $libm_extralibs
# enabled libmysofa         && { check_pkg_config libmysofa libmysofa mysofa.h mysofa_load ||
#                                require libmysofa mysofa.h mysofa_load -lmysofa $zlib_extralibs; }
# enabled libnpp            && { check_lib libnpp npp.h nppGetLibVersion -lnppig -lnppicc -lnppc -lnppidei ||
#                                check_lib libnpp npp.h nppGetLibVersion -lnppi -lnppc -lnppidei ||
#                                die "ERROR: libnpp not found"; }
# enabled libopencore_amrnb && require libopencore_amrnb opencore-amrnb/interf_dec.h Decoder_Interface_init -lopencore-amrnb
# enabled libopencore_amrwb && require libopencore_amrwb opencore-amrwb/dec_if.h D_IF_init -lopencore-amrwb
# enabled libopencv         && { check_headers opencv2/core/core_c.h &&
#                                { check_pkg_config libopencv opencv opencv2/core/core_c.h cvCreateImageHeader ||
#                                  require libopencv opencv2/core/core_c.h cvCreateImageHeader -lopencv_core -lopencv_imgproc; } ||
#                                require_pkg_config libopencv opencv opencv/cxcore.h cvCreateImageHeader; }
# enabled libopenh264       && require_pkg_config libopenh264 openh264 wels/codec_api.h WelsGetCodecVersion
# enabled libopenjpeg       && { check_pkg_config libopenjpeg "libopenjp2 >= 2.1.0" openjpeg.h opj_version ||
#                                { require_pkg_config libopenjpeg "libopenjp2 >= 2.1.0" openjpeg.h opj_version -DOPJ_STATIC && add_cppflags -DOPJ_STATIC; } }
# enabled libopenmpt        && require_pkg_config libopenmpt "libopenmpt >= 0.2.6557" libopenmpt/libopenmpt.h openmpt_module_create -lstdc++ && append libopenmpt_extralibs "-lstdc++"
# enabled libopus           && {
#     enabled libopus_decoder && {
#         require_pkg_config libopus opus opus_multistream.h opus_multistream_decoder_create
#     }
#     enabled libopus_encoder && {
#         require_pkg_config libopus opus opus_multistream.h opus_multistream_surround_encoder_create
#     }
# }
# enabled libpulse          && require_pkg_config libpulse libpulse pulse/pulseaudio.h pa_context_new
# enabled librsvg           && require_pkg_config librsvg librsvg-2.0 librsvg-2.0/librsvg/rsvg.h rsvg_handle_render_cairo
# enabled librtmp           && require_pkg_config librtmp librtmp librtmp/rtmp.h RTMP_Socket
# enabled librubberband     && require_pkg_config librubberband "rubberband >= 1.8.1" rubberband/rubberband-c.h rubberband_new -lstdc++ && append librubberband_extralibs "-lstdc++"
# enabled libshine          && require_pkg_config libshine shine shine/layer3.h shine_encode_buffer
# enabled libsmbclient      && { check_pkg_config libsmbclient smbclient libsmbclient.h smbc_init ||
#                                require libsmbclient libsmbclient.h smbc_init -lsmbclient; }
# enabled libsnappy         && require libsnappy snappy-c.h snappy_compress -lsnappy -lstdc++
# enabled libsoxr           && require libsoxr soxr.h soxr_create -lsoxr
# enabled libssh            && require_pkg_config libssh libssh libssh/sftp.h sftp_init
# enabled libspeex          && require_pkg_config libspeex speex speex/speex.h speex_decoder_init
# enabled libsrt            && require_pkg_config libsrt "srt >= 1.3.0" srt/srt.h srt_socket
# enabled libtensorflow     && require libtensorflow tensorflow/c/c_api.h TF_Version -ltensorflow
# enabled libtesseract      && require_pkg_config libtesseract tesseract tesseract/capi.h TessBaseAPICreate
# enabled libtheora         && require libtheora theora/theoraenc.h th_info_init -ltheoraenc -ltheoradec -logg
# enabled libtls            && require_pkg_config libtls libtls tls.h tls_configure
# enabled libtwolame        && require libtwolame twolame.h twolame_init -ltwolame &&
#                              { check_lib libtwolame twolame.h twolame_encode_buffer_float32_interleaved -ltwolame ||
#                                die "ERROR: libtwolame must be installed and version must be >= 0.3.10"; }
# enabled libv4l2           && require_pkg_config libv4l2 libv4l2 libv4l2.h v4l2_ioctl
# enabled libvidstab        && require_pkg_config libvidstab "vidstab >= 0.98" vid.stab/libvidstab.h vsMotionDetectInit
# enabled libvmaf           && require_pkg_config libvmaf "libvmaf >= 1.3.9" libvmaf.h compute_vmaf
# enabled libvo_amrwbenc    && require libvo_amrwbenc vo-amrwbenc/enc_if.h E_IF_init -lvo-amrwbenc
# enabled libvorbis         && require_pkg_config libvorbis vorbis vorbis/codec.h vorbis_info_init &&
#                              require_pkg_config libvorbisenc vorbisenc vorbis/vorbisenc.h vorbis_encode_init

# enabled libvpx            && {
#     enabled libvpx_vp8_decoder && {
#         check_pkg_config libvpx_vp8_decoder "vpx >= 1.4.0" "vpx/vpx_decoder.h vpx/vp8dx.h" vpx_codec_vp8_dx ||
#             check_lib libvpx_vp8_decoder "vpx/vpx_decoder.h vpx/vp8dx.h" "vpx_codec_vp8_dx VPX_IMG_FMT_HIGHBITDEPTH" "-lvpx $libm_extralibs $pthreads_extralibs"
#     }
#     enabled libvpx_vp8_encoder && {
#         check_pkg_config libvpx_vp8_encoder "vpx >= 1.4.0" "vpx/vpx_encoder.h vpx/vp8cx.h" vpx_codec_vp8_cx ||
#             check_lib libvpx_vp8_encoder "vpx/vpx_encoder.h vpx/vp8cx.h" "vpx_codec_vp8_cx VPX_IMG_FMT_HIGHBITDEPTH" "-lvpx $libm_extralibs $pthreads_extralibs"
#     }
#     enabled libvpx_vp9_decoder && {
#         check_pkg_config libvpx_vp9_decoder "vpx >= 1.4.0" "vpx/vpx_decoder.h vpx/vp8dx.h" vpx_codec_vp9_dx ||
#             check_lib libvpx_vp9_decoder "vpx/vpx_decoder.h vpx/vp8dx.h" "vpx_codec_vp9_dx VPX_IMG_FMT_HIGHBITDEPTH" "-lvpx $libm_extralibs $pthreads_extralibs"
#     }
#     enabled libvpx_vp9_encoder && {
#         check_pkg_config libvpx_vp9_encoder "vpx >= 1.4.0" "vpx/vpx_encoder.h vpx/vp8cx.h" vpx_codec_vp9_cx ||
#             check_lib libvpx_vp9_encoder "vpx/vpx_encoder.h vpx/vp8cx.h" "vpx_codec_vp9_cx VPX_IMG_FMT_HIGHBITDEPTH" "-lvpx $libm_extralibs $pthreads_extralibs"
#     }
#     if disabled_all libvpx_vp8_decoder libvpx_vp9_decoder libvpx_vp8_encoder libvpx_vp9_encoder; then
#         die "libvpx enabled but no supported decoders found"
#     fi
# }

# enabled libwavpack        && require libwavpack wavpack/wavpack.h WavpackOpenFileOutput  -lwavpack
# enabled libwebp           && {
#     enabled libwebp_encoder      && require_pkg_config libwebp "libwebp >= 0.2.0" webp/encode.h WebPGetEncoderVersion
#     enabled libwebp_anim_encoder && check_pkg_config libwebp_anim_encoder "libwebpmux >= 0.4.0" webp/mux.h WebPAnimEncoderOptionsInit; }
# enabled libx264           && { check_pkg_config libx264 x264 "stdint.h x264.h" x264_encoder_encode ||
#                                { require libx264 "stdint.h x264.h" x264_encoder_encode "-lx264 $pthreads_extralibs $libm_extralibs" &&
#                                  warn "using libx264 without pkg-config"; } } &&
#                              require_cpp_condition libx264 x264.h "X264_BUILD >= 118" &&
#                              check_cpp_condition libx262 x264.h "X264_MPEG2"
# enabled libx265           && require_pkg_config libx265 x265 x265.h x265_api_get &&
#                              require_cpp_condition libx265 x265.h "X265_BUILD >= 68"
# enabled libxavs           && require libxavs "stdint.h xavs.h" xavs_encoder_encode "-lxavs $pthreads_extralibs $libm_extralibs"
# enabled libxavs2          && require_pkg_config libxavs2 "xavs2 >= 1.3.0" "stdint.h xavs2.h" xavs2_api_get
# enabled libxvid           && require libxvid xvid.h xvid_global -lxvidcore
# enabled libzimg           && require_pkg_config libzimg "zimg >= 2.7.0" zimg.h zimg_get_api_version
# enabled libzmq            && require_pkg_config libzmq libzmq zmq.h zmq_ctx_new
# enabled libzvbi           && require_pkg_config libzvbi zvbi-0.2 libzvbi.h vbi_decoder_new &&
#                              { test_cpp_condition libzvbi.h "VBI_VERSION_MAJOR > 0 || VBI_VERSION_MINOR > 2 || VBI_VERSION_MINOR == 2 && VBI_VERSION_MICRO >= 28" ||
#                                enabled gpl || die "ERROR: libzvbi requires version 0.2.28 or --enable-gpl."; }
# enabled libxml2           && require_pkg_config libxml2 libxml-2.0 libxml2/libxml/xmlversion.h xmlCheckVersion
# enabled mbedtls           && { check_pkg_config mbedtls mbedtls mbedtls/x509_crt.h mbedtls_x509_crt_init ||
#                                check_pkg_config mbedtls mbedtls mbedtls/ssl.h mbedtls_ssl_init ||
#                                check_lib mbedtls mbedtls/ssl.h mbedtls_ssl_init -lmbedtls -lmbedx509 -lmbedcrypto ||
#                                die "ERROR: mbedTLS not found"; }
# enabled mediacodec        && { enabled jni || die "ERROR: mediacodec requires --enable-jni"; }
# enabled mmal              && { check_lib mmal interface/mmal/mmal.h mmal_port_connect -lmmal_core -lmmal_util -lmmal_vc_client -lbcm_host ||
#                                { ! enabled cross_compile &&
#                                  add_cflags -isystem/opt/vc/include/ -isystem/opt/vc/include/interface/vmcs_host/linux -isystem/opt/vc/include/interface/vcos/pthreads -fgnu89-inline &&
#                                  add_ldflags -L/opt/vc/lib/ &&
#                                  check_lib mmal interface/mmal/mmal.h mmal_port_connect -lmmal_core -lmmal_util -lmmal_vc_client -lbcm_host; } ||
#                                die "ERROR: mmal not found" &&
#                                check_func_headers interface/mmal/mmal.h "MMAL_PARAMETER_VIDEO_MAX_NUM_CALLBACKS"; }
# enabled openal            && { { for al_extralibs in "${OPENAL_LIBS}" "-lopenal" "-lOpenAL32"; do
#                                check_lib openal 'AL/al.h' alGetError "${al_extralibs}" && break; done } ||
#                                die "ERROR: openal not found"; } &&
#                              { test_cpp_condition "AL/al.h" "defined(AL_VERSION_1_1)" ||
#                                die "ERROR: openal must be installed and version must be 1.1 or compatible"; }
# enabled opencl            && { check_pkg_config opencl OpenCL CL/cl.h clEnqueueNDRangeKernel ||
#                                check_lib opencl OpenCL/cl.h clEnqueueNDRangeKernel -Wl,-framework,OpenCL ||
#                                check_lib opencl CL/cl.h clEnqueueNDRangeKernel -lOpenCL ||
#                                die "ERROR: opencl not found"; } &&
#                              { test_cpp_condition "OpenCL/cl.h" "defined(CL_VERSION_1_2)" ||
#                                test_cpp_condition "CL/cl.h" "defined(CL_VERSION_1_2)" ||
#                                die "ERROR: opencl must be installed and version must be 1.2 or compatible"; }
# enabled opengl            && { check_lib opengl GL/glx.h glXGetProcAddress "-lGL" ||
#                                check_lib opengl windows.h wglGetProcAddress "-lopengl32 -lgdi32" ||
#                                check_lib opengl OpenGL/gl3.h glGetError "-Wl,-framework,OpenGL" ||
#                                check_lib opengl ES2/gl.h glGetError "-isysroot=${sysroot} -Wl,-framework,OpenGLES" ||
#                                die "ERROR: opengl not found."
#                              }
# enabled omx               && require_headers OMX_Core.h
# enabled omx_rpi           && { check_headers OMX_Core.h ||
#                                { ! enabled cross_compile && add_cflags -isystem/opt/vc/include/IL && check_headers OMX_Core.h ; } ||
#                                die "ERROR: OpenMAX IL headers not found"; } && enable omx
# enabled openssl           && { check_pkg_config openssl openssl openssl/ssl.h OPENSSL_init_ssl ||
#                                check_pkg_config openssl openssl openssl/ssl.h SSL_library_init ||
#                                check_lib openssl openssl/ssl.h SSL_library_init -lssl -lcrypto ||
#                                check_lib openssl openssl/ssl.h SSL_library_init -lssl32 -leay32 ||
#                                check_lib openssl openssl/ssl.h SSL_library_init -lssl -lcrypto -lws2_32 -lgdi32 ||
#                                die "ERROR: openssl not found"; }
# enabled pocketsphinx      && require_pkg_config pocketsphinx pocketsphinx pocketsphinx/pocketsphinx.h ps_init
# enabled rkmpp             && { require_pkg_config rkmpp rockchip_mpp  rockchip/rk_mpi.h mpp_create &&
#                                require_pkg_config rockchip_mpp "rockchip_mpp >= 1.3.7" rockchip/rk_mpi.h mpp_create &&
#                                { enabled libdrm ||
#                                  die "ERROR: rkmpp requires --enable-libdrm"; }
#                              }
# enabled vapoursynth       && require_pkg_config vapoursynth "vapoursynth-script >= 42" VSScript.h vsscript_init


# if enabled gcrypt; then
#     GCRYPT_CONFIG="${cross_prefix}libgcrypt-config"
#     if "${GCRYPT_CONFIG}" --version > /dev/null 2>&1; then
#         gcrypt_cflags=$("${GCRYPT_CONFIG}" --cflags)
#         gcrypt_extralibs=$("${GCRYPT_CONFIG}" --libs)
#         check_func_headers gcrypt.h gcry_mpi_new $gcrypt_cflags $gcrypt_extralibs ||
#             die "ERROR: gcrypt not found"
#         add_cflags $gcrypt_cflags
#     else
#         require gcrypt gcrypt.h gcry_mpi_new -lgcrypt
#     fi
# fi

# if enabled sdl2; then
#     SDL2_CONFIG="${cross_prefix}sdl2-config"
#     test_pkg_config sdl2 "sdl2 >= 2.0.1 sdl2 < 2.1.0" SDL_events.h SDL_PollEvent
#     if disabled sdl2 && "${SDL2_CONFIG}" --version > /dev/null 2>&1; then
#         sdl2_cflags=$("${SDL2_CONFIG}" --cflags)
#         sdl2_extralibs=$("${SDL2_CONFIG}" --libs)
#         test_cpp_condition SDL.h "(SDL_MAJOR_VERSION<<16 | SDL_MINOR_VERSION<<8 | SDL_PATCHLEVEL) >= 0x020001" $sdl2_cflags &&
#         test_cpp_condition SDL.h "(SDL_MAJOR_VERSION<<16 | SDL_MINOR_VERSION<<8 | SDL_PATCHLEVEL) < 0x020100" $sdl2_cflags &&
#         check_func_headers SDL_events.h SDL_PollEvent $sdl2_extralibs $sdl2_cflags &&
#             enable sdl2
#     fi
#     if test $target_os = "mingw32"; then
#         sdl2_extralibs=$(filter_out '-mwindows' $sdl2_extralibs)
#     fi
# fi

# if enabled decklink; then
#     case $target_os in
#         mingw32*|mingw64*|win32|win64)
#             decklink_outdev_extralibs="$decklink_outdev_extralibs -lole32 -loleaut32"
#             decklink_indev_extralibs="$decklink_indev_extralibs -lole32 -loleaut32"
#             ;;
#     esac
# fi

# enabled securetransport &&
#     check_func SecIdentityCreate "-Wl,-framework,CoreFoundation -Wl,-framework,Security" &&
#     check_lib securetransport "Security/SecureTransport.h Security/Security.h" "SSLCreateContext" "-Wl,-framework,CoreFoundation -Wl,-framework,Security" ||
#         disable securetransport

# enabled securetransport &&
#     check_func SecItemImport "-Wl,-framework,CoreFoundation -Wl,-framework,Security"

# enabled schannel &&
#     check_func_headers "windows.h security.h" InitializeSecurityContext -DSECURITY_WIN32 -lsecur32 &&
#     test_cpp_condition winerror.h "defined(SEC_I_CONTEXT_EXPIRED)" &&
#     schannel_extralibs="-lsecur32" ||
#         disable schannel

# makeinfo --version > /dev/null 2>&1 && enable makeinfo  || disable makeinfo
# enabled makeinfo \
#     && [ 0$(makeinfo --version | grep "texinfo" | sed 's/.*texinfo[^0-9]*\([0-9]*\)\..*/\1/') -ge 5 ] \
#     && enable makeinfo_html || disable makeinfo_html
# disabled makeinfo_html && texi2html --help 2> /dev/null | grep -q 'init-file' && enable texi2html || disable texi2html
# perl -v            > /dev/null 2>&1 && enable perl      || disable perl
# pod2man --help     > /dev/null 2>&1 && enable pod2man   || disable pod2man
# rsync --help 2> /dev/null | grep -q 'contimeout' && enable rsync_contimeout || disable rsync_contimeout

# # check V4L2 codecs available in the API
# check_headers linux/fb.h
# check_headers linux/videodev2.h
# test_code cc linux/videodev2.h "struct v4l2_frmsizeenum vfse; vfse.discrete.width = 0;" && enable_sanitized struct_v4l2_frmivalenum_discrete
# check_cc v4l2_m2m linux/videodev2.h "int i = V4L2_CAP_VIDEO_M2M_MPLANE | V4L2_CAP_VIDEO_M2M | V4L2_BUF_FLAG_LAST;"
# check_cc vc1_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_VC1_ANNEX_G;"
# check_cc mpeg1_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_MPEG1;"
# check_cc mpeg2_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_MPEG2;"
# check_cc mpeg4_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_MPEG4;"
# check_cc hevc_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_HEVC;"
# check_cc h263_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_H263;"
# check_cc h264_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_H264;"
# check_cc vp8_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_VP8;"
# check_cc vp9_v4l2_m2m linux/videodev2.h "int i = V4L2_PIX_FMT_VP9;"

# check_headers sys/videoio.h
# test_code cc sys/videoio.h "struct v4l2_frmsizeenum vfse; vfse.discrete.width = 0;" && enable_sanitized struct_v4l2_frmivalenum_discrete

# check_lib user32 "windows.h winuser.h" GetShellWindow -luser32
# check_lib vfw32 "windows.h vfw.h" capCreateCaptureWindow -lvfw32
# # check that WM_CAP_DRIVER_CONNECT is defined to the proper value
# # w32api 3.12 had it defined wrong
# check_cpp_condition vfwcap_defines vfw.h "WM_CAP_DRIVER_CONNECT > WM_USER"

# check_type "dshow.h" IBaseFilter

# # check for ioctl_meteor.h, ioctl_bt848.h and alternatives
# check_headers "dev/bktr/ioctl_meteor.h dev/bktr/ioctl_bt848.h"                   ||
#     check_headers "machine/ioctl_meteor.h machine/ioctl_bt848.h"                 ||
#     check_headers "dev/video/meteor/ioctl_meteor.h dev/video/bktr/ioctl_bt848.h" ||
#     check_headers "dev/ic/bt8xx.h"

# if check_struct sys/soundcard.h audio_buf_info bytes; then
#     enable_sanitized sys/soundcard.h
# else
#     test_cc -D__BSD_VISIBLE -D__XSI_VISIBLE <<EOF && add_cppflags -D__BSD_VISIBLE -D__XSI_VISIBLE && enable_sanitized sys/soundcard.h
#     #include <sys/soundcard.h>
#     audio_buf_info abc;
# EOF
# fi

# enabled alsa && check_pkg_config alsa alsa "alsa/asoundlib.h" snd_pcm_htimestamp ||
#     check_lib alsa alsa/asoundlib.h snd_pcm_htimestamp -lasound

# enabled libjack &&
#     require_pkg_config libjack jack jack/jack.h jack_port_get_latency_range

# enabled sndio && check_lib sndio sndio.h sio_open -lsndio

# if enabled libcdio; then
#     check_pkg_config libcdio libcdio_paranoia "cdio/cdda.h cdio/paranoia.h" cdio_cddap_open ||
#     check_pkg_config libcdio libcdio_paranoia "cdio/paranoia/cdda.h cdio/paranoia/paranoia.h" cdio_cddap_open ||
#     check_lib libcdio "cdio/cdda.h cdio/paranoia.h" cdio_cddap_open -lcdio_paranoia -lcdio_cdda -lcdio ||
#     check_lib libcdio "cdio/paranoia/cdda.h cdio/paranoia/paranoia.h" cdio_cddap_open -lcdio_paranoia -lcdio_cdda -lcdio ||
#     die "ERROR: No usable libcdio/cdparanoia found"
# fi

# enabled libxcb && check_pkg_config libxcb "xcb >= 1.4" xcb/xcb.h xcb_connect ||
#     disable libxcb_shm libxcb_shape libxcb_xfixes

# if enabled libxcb; then
#     enabled libxcb_shm    && check_pkg_config libxcb_shm    xcb-shm    xcb/shm.h    xcb_shm_attach
#     enabled libxcb_shape  && check_pkg_config libxcb_shape  xcb-shape  xcb/shape.h  xcb_shape_get_rectangles
#     enabled libxcb_xfixes && check_pkg_config libxcb_xfixes xcb-xfixes xcb/xfixes.h xcb_xfixes_get_cursor_image
# fi

# check_func_headers "windows.h" CreateDIBSection "$gdigrab_indev_extralibs"

# # d3d11va requires linking directly to dxgi and d3d11 if not building for
# # the desktop api partition
# test_cpp <<EOF && enable uwp && d3d11va_extralibs="-ldxgi -ld3d11"
# #ifdef WINAPI_FAMILY
# #include <winapifamily.h>
# #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# #error desktop, not uwp
# #else
# // WINAPI_FAMILY_APP, WINAPI_FAMILY_PHONE_APP => UWP
# #endif
# #else
# #error no family set
# #endif
# EOF

# enabled vaapi &&
#     check_pkg_config vaapi "libva >= 0.35.0" "va/va.h" vaInitialize

# if enabled vaapi; then
#     check_pkg_config vaapi_drm "libva-drm" "va/va_drm.h" vaGetDisplayDRM

#     if enabled xlib; then
#         check_pkg_config vaapi_x11 "libva-x11" "va/va_x11.h" vaGetDisplay
#     fi

#     check_cpp_condition vaapi_1 "va/va.h" "VA_CHECK_VERSION(1, 0, 0)"

#     check_type "va/va.h va/va_dec_hevc.h" "VAPictureParameterBufferHEVC"
#     check_struct "va/va.h" "VADecPictureParameterBufferVP9" bit_depth
#     check_struct "va/va.h va/va_vpp.h" "VAProcPipelineCaps" rotation_flags
#     check_type "va/va.h va/va_enc_hevc.h" "VAEncPictureParameterBufferHEVC"
#     check_type "va/va.h va/va_enc_jpeg.h" "VAEncPictureParameterBufferJPEG"
#     check_type "va/va.h va/va_enc_vp8.h"  "VAEncPictureParameterBufferVP8"
#     check_type "va/va.h va/va_enc_vp9.h"  "VAEncPictureParameterBufferVP9"
# fi

# if enabled_all opencl libdrm ; then
#     check_type "CL/cl_intel.h" "clCreateImageFromFdINTEL_fn" &&
#         enable opencl_drm_beignet
#     check_func_headers "CL/cl_ext.h" clImportMemoryARM &&
#         enable opencl_drm_arm
# fi

# if enabled_all opencl vaapi ; then
#     if enabled opencl_drm_beignet ; then
#         enable opencl_vaapi_beignet
#     else
#         check_type "CL/cl.h CL/cl_va_api_media_sharing_intel.h" "clCreateFromVA_APIMediaSurfaceINTEL_fn" &&
#             enable opencl_vaapi_intel_media
#     fi
# fi

# if enabled_all opencl dxva2 ; then
#     check_type "CL/cl_dx9_media_sharing.h" cl_dx9_surface_info_khr &&
#         enable opencl_dxva2
# fi

# if enabled_all opencl d3d11va ; then
#     check_type "CL/cl_d3d11.h" clGetDeviceIDsFromD3D11KHR_fn &&
#         enable opencl_d3d11
# fi

# enabled vdpau &&
#     check_cpp_condition vdpau vdpau/vdpau.h "defined VDP_DECODER_PROFILE_MPEG4_PART2_ASP"

# enabled vdpau &&
#     check_lib vdpau_x11 "vdpau/vdpau.h vdpau/vdpau_x11.h" vdp_device_create_x11 -lvdpau -lX11

# enabled crystalhd && check_lib crystalhd "stdint.h libcrystalhd/libcrystalhd_if.h" DtsCrystalHDVersion -lcrystalhd

# if enabled x86; then
#     case $target_os in
#         mingw32*|mingw64*|win32|win64|linux|cygwin*)
#             ;;
#         *)
#             disable ffnvcodec cuvid nvdec nvenc
#             ;;
#     esac
# elif enabled ppc64 && ! enabled bigendian; then
#     case $target_os in
#         linux)
#             ;;
#         *)
#             disable ffnvcodec cuvid nvdec nvenc
#             ;;
#     esac
# else
#     disable ffnvcodec cuvid nvdec nvenc
# fi

# enabled ffnvcodec && enable cuda

# enabled nvenc &&
#     test_cc -I$source_path <<EOF || disable nvenc
# #include <ffnvcodec/nvEncodeAPI.h>
# NV_ENCODE_API_FUNCTION_LIST flist;
# void f(void) { struct { const GUID guid; } s[] = { { NV_ENC_PRESET_HQ_GUID } }; }
# int main(void) { return 0; }
# EOF

# enabled amf &&
#     check_cpp_condition amf "AMF/core/Version.h" \
#         "(AMF_VERSION_MAJOR << 48 | AMF_VERSION_MINOR << 32 | AMF_VERSION_RELEASE << 16 | AMF_VERSION_BUILD_NUM) >= 0x0001000400040001"

# # Funny iconv installations are not unusual, so check it after all flags have been set
# if enabled libc_iconv; then
#     check_func_headers iconv.h iconv
# elif enabled iconv; then
#     check_func_headers iconv.h iconv || check_lib iconv iconv.h iconv -liconv
# fi

# enabled debug && add_cflags -g"$debuglevel" && add_asflags -g"$debuglevel"

# # add some useful compiler flags if supported
# check_cflags -Wdeclaration-after-statement
# check_cflags -Wall
# check_cflags -Wdisabled-optimization
# check_cflags -Wpointer-arith
# check_cflags -Wredundant-decls
# check_cflags -Wwrite-strings
# check_cflags -Wtype-limits
# check_cflags -Wundef
# check_cflags -Wmissing-prototypes
# check_cflags -Wno-pointer-to-int-cast
# check_cflags -Wstrict-prototypes
# check_cflags -Wempty-body

# if enabled extra_warnings; then
#     check_cflags -Wcast-qual
#     check_cflags -Wextra
#     check_cflags -Wpedantic
# fi

# check_disable_warning(){
#     warning_flag=-W${1#-Wno-}
#     test_cflags $unknown_warning_flags $warning_flag && add_cflags $1
# }

# test_cflags -Werror=unused-command-line-argument &&
#     append unknown_warning_flags "-Werror=unused-command-line-argument"
# test_cflags -Werror=unknown-warning-option &&
#     append unknown_warning_flags "-Werror=unknown-warning-option"

# check_disable_warning -Wno-parentheses
# check_disable_warning -Wno-switch
# check_disable_warning -Wno-format-zero-length
# check_disable_warning -Wno-pointer-sign
# check_disable_warning -Wno-unused-const-variable
# check_disable_warning -Wno-bool-operation
# check_disable_warning -Wno-char-subscripts

# check_disable_warning_headers(){
#     warning_flag=-W${1#-Wno-}
#     test_cflags $warning_flag && add_cflags_headers $1
# }

# check_disable_warning_headers -Wno-deprecated-declarations
# check_disable_warning_headers -Wno-unused-variable

# test_cc <<EOF && enable blocks_extension
# void (^block)(void);
# EOF

# # add some linker flags
# check_ldflags -Wl,--warn-common
# check_ldflags -Wl,-rpath-link=:libpostproc:libswresample:libswscale:libavfilter:libavdevice:libavformat:libavcodec:libavutil:libavresample
# enabled rpath && add_ldexeflags -Wl,-rpath,$libdir && add_ldsoflags -Wl,-rpath,$libdir
# test_ldflags -Wl,-Bsymbolic && append SHFLAGS -Wl,-Bsymbolic

# # add some strip flags
# check_stripflags -x

# enabled neon_clobber_test &&
#     check_ldflags -Wl,--wrap,avcodec_open2              \
#                   -Wl,--wrap,avcodec_decode_audio4      \
#                   -Wl,--wrap,avcodec_decode_video2      \
#                   -Wl,--wrap,avcodec_decode_subtitle2   \
#                   -Wl,--wrap,avcodec_encode_audio2      \
#                   -Wl,--wrap,avcodec_encode_video2      \
#                   -Wl,--wrap,avcodec_encode_subtitle    \
#                   -Wl,--wrap,avcodec_send_packet        \
#                   -Wl,--wrap,avcodec_receive_packet     \
#                   -Wl,--wrap,avcodec_send_frame         \
#                   -Wl,--wrap,avcodec_receive_frame      \
#                   -Wl,--wrap,swr_convert                \
#                   -Wl,--wrap,avresample_convert ||
#     disable neon_clobber_test

# enabled xmm_clobber_test &&
#     check_ldflags -Wl,--wrap,avcodec_open2              \
#                   -Wl,--wrap,avcodec_decode_audio4      \
#                   -Wl,--wrap,avcodec_decode_video2      \
#                   -Wl,--wrap,avcodec_decode_subtitle2   \
#                   -Wl,--wrap,avcodec_encode_audio2      \
#                   -Wl,--wrap,avcodec_encode_video2      \
#                   -Wl,--wrap,avcodec_encode_subtitle    \
#                   -Wl,--wrap,avcodec_send_packet        \
#                   -Wl,--wrap,avcodec_receive_packet     \
#                   -Wl,--wrap,avcodec_send_frame         \
#                   -Wl,--wrap,avcodec_receive_frame      \
#                   -Wl,--wrap,swr_convert                \
#                   -Wl,--wrap,avresample_convert         \
#                   -Wl,--wrap,sws_scale ||
#     disable xmm_clobber_test

# check_ld "cc" proper_dce <<EOF
# extern const int array[512];
# static inline int func(void) { return array[0]; }
# int main(void) { return 0; }
# EOF

# if enabled proper_dce; then
#     echo "X { local: *; };" > $TMPV
#     if test_ldflags -Wl,${version_script},$TMPV; then
#         append SHFLAGS '-Wl,${version_script},\$(SUBDIR)lib\$(NAME).ver'
#         quotes='""'
#         test_cc <<EOF && enable symver_asm_label
# void ff_foo(void) __asm__ ("av_foo@VERSION");
# void ff_foo(void) { ${inline_asm+__asm__($quotes);} }
# EOF
#         test_cc <<EOF && enable symver_gnu_asm
# __asm__(".symver ff_foo,av_foo@VERSION");
# void ff_foo(void) {}
# EOF
#     fi
# fi

# if [ -z "$optflags" ]; then
#     if enabled small; then
#         optflags=$cflags_size
#     elif enabled optimizations; then
#         optflags=$cflags_speed
#     else
#         optflags=$cflags_noopt
#     fi
# fi

# check_optflags(){
#     check_cflags "$@"
#     enabled lto && check_ldflags "$@"
# }

# check_optflags $optflags
# check_optflags -fno-math-errno
# check_optflags -fno-signed-zeros

# if enabled lto; then
#     test "$cc_type" != "$ld_type" && die "LTO requires same compiler and linker"
#     check_cflags  -flto
#     check_ldflags -flto $cpuflags
#     disable inline_asm_direct_symbol_refs
# fi

# enabled ftrapv && check_cflags -ftrapv

# test_cc -mno-red-zone <<EOF && noredzone_flags="-mno-red-zone"
# int x;
# EOF


# if enabled icc; then
#     # Just warnings, no remarks
#     check_cflags -w1
#     # -wd: Disable following warnings
#     # 144, 167, 556: -Wno-pointer-sign
#     # 188: enumerated type mixed with another type
#     # 1292: attribute "foo" ignored
#     # 1419: external declaration in primary source file
#     # 10006: ignoring unknown option -fno-signed-zeros
#     # 10148: ignoring unknown option -Wno-parentheses
#     # 10156: ignoring option '-W'; no argument required
#     # 13200: No EMMS instruction before call to function
#     # 13203: No EMMS instruction before return from function
#     check_cflags -wd144,167,188,556,1292,1419,10006,10148,10156,13200,13203
#     # 11030: Warning unknown option --as-needed
#     # 10156: ignoring option '-export'; no argument required
#     check_ldflags -wd10156,11030
#     # icc 11.0 and 11.1 work with ebp_available, but don't pass the test
#     enable ebp_available
#     # The test above does not test linking
#     enabled lto && disable symver_asm_label
#     if enabled x86_32; then
#         icc_version=$($cc -dumpversion)
#         test ${icc_version%%.*} -ge 11 &&
#             check_cflags -falign-stack=maintain-16-byte ||
#             disable aligned_stack
#     fi
# elif enabled gcc; then
#     check_optflags -fno-tree-vectorize
#     check_cflags -Werror=format-security
#     check_cflags -Werror=implicit-function-declaration
#     check_cflags -Werror=missing-prototypes
#     check_cflags -Werror=return-type
#     check_cflags -Werror=vla
#     check_cflags -Wformat
#     check_cflags -fdiagnostics-color=auto
#     enabled extra_warnings || check_disable_warning -Wno-maybe-uninitialized
#     if enabled x86_32; then
#         case $target_os in
#         *bsd*)
#             # BSDs don't guarantee a 16 byte aligned stack, but we can
#             # request GCC to try to maintain 16 byte alignment throughout
#             # function calls. Library entry points that might call assembly
#             # functions align the stack. (The parameter means 2^4 bytes.)
#             check_cflags -mpreferred-stack-boundary=4
#             ;;
#         esac
#     fi
# elif enabled llvm_gcc; then
#     check_cflags -mllvm -stack-alignment=16
# elif enabled clang; then
#     if enabled x86_32; then
#         # Clang doesn't support maintaining alignment without assuming the
#         # same alignment in every function. If 16 byte alignment would be
#         # enabled, one would also have to either add attribute_align_arg on
#         # every single entry point into the libraries or enable -mstackrealign
#         # (doing stack realignment in every single function).
#         case $target_os in
#         mingw32|win32|*bsd*)
#             disable aligned_stack
#             ;;
#         *)
#             check_cflags -mllvm -stack-alignment=16
#             check_cflags -mstack-alignment=16
#             ;;
#         esac
#     else
#         check_cflags -mllvm -stack-alignment=16
#         check_cflags -mstack-alignment=16
#     fi
#     check_cflags -Qunused-arguments
#     check_cflags -Werror=implicit-function-declaration
#     check_cflags -Werror=missing-prototypes
#     check_cflags -Werror=return-type
# elif enabled cparser; then
#     add_cflags -Wno-missing-variable-declarations
#     add_cflags -Wno-empty-statement
# elif enabled armcc; then
#     add_cflags -W${armcc_opt},--diag_suppress=4343 # hardfp compat
#     add_cflags -W${armcc_opt},--diag_suppress=3036 # using . as system include dir
#     # 2523: use of inline assembly is deprecated
#     add_cflags -W${armcc_opt},--diag_suppress=2523
#     add_cflags -W${armcc_opt},--diag_suppress=1207
#     add_cflags -W${armcc_opt},--diag_suppress=1293 # assignment in condition
#     add_cflags -W${armcc_opt},--diag_suppress=3343 # hardfp compat
#     add_cflags -W${armcc_opt},--diag_suppress=167  # pointer sign
#     add_cflags -W${armcc_opt},--diag_suppress=513  # pointer sign
# elif enabled pathscale; then
#     add_cflags -fstrict-overflow -OPT:wrap_around_unsafe_opt=OFF
#     disable inline_asm
# elif enabled_any msvc icl; then
#     enabled x86_32 && disable aligned_stack
#     enabled_all x86_32 debug && add_cflags -Oy-
#     enabled debug && add_ldflags -debug
#     enable pragma_deprecated
#     if enabled icl; then
#         # -Qansi-alias is basically -fstrict-aliasing, but does not work
#         # (correctly) on icl 13.x.
#         test_cpp_condition "windows.h" "__ICL < 1300 || __ICL >= 1400" &&
#             add_cflags -Qansi-alias
#         # Some inline asm is not compilable in debug
#         if enabled debug; then
#             disable ebp_available
#             disable ebx_available
#         fi
#     fi
#     # msvcrt10 x64 incorrectly enables log2, only msvcrt12 (MSVC 2013) onwards actually has log2.
#     check_cpp_condition log2 crtversion.h "_VC_CRT_MAJOR_VERSION >= 12"
#     # The CRT headers contain __declspec(restrict) in a few places, but if redefining
#     # restrict, this might break. MSVC 2010 and 2012 fail with __declspec(__restrict)
#     # (as it ends up if the restrict redefine is done before including stdlib.h), while
#     # MSVC 2013 and newer can handle it fine.
#     # If this declspec fails, force including stdlib.h before the restrict redefinition
#     # happens in config.h.
#     if [ $restrict_keyword != restrict ]; then
#         test_cc <<EOF || add_cflags -FIstdlib.h
# __declspec($restrict_keyword) void *foo(int);
# EOF
#     fi
#     # the new SSA optimzer in VS2015 U3 is mis-optimizing some parts of the code
#     # Issue has been fixed in MSVC v19.00.24218.
#     test_cpp_condition windows.h "_MSC_FULL_VER >= 190024218" ||
#         check_cflags -d2SSAOptimizer-
#     # enable utf-8 source processing on VS2015 U2 and newer
#     test_cpp_condition windows.h "_MSC_FULL_VER >= 190023918" &&
#         add_cflags -utf-8
# fi

# for pfx in "" host_; do
#     varname=${pfx%_}cc_type
#     eval "type=\$$varname"
#     if [ "$type" = "msvc" ]; then
#         test_${pfx}cc <<EOF || add_${pfx}cflags -Dinline=__inline
# static inline int foo(int a) { return a; }
# EOF
#     fi
# done

# case $as_type in
#     clang)
#         add_asflags -Qunused-arguments
#     ;;
# esac

# case $ld_type in
#     clang)
#         check_ldflags -Qunused-arguments
#     ;;
# esac

# enable frame_thread_encoder

# enabled asm || { arch=c; disable $ARCH_LIST $ARCH_EXT_LIST; }

# check_deps $CONFIG_LIST       \
#            $CONFIG_EXTRA      \
#            $HAVE_LIST         \
#            $ALL_COMPONENTS    \

# enabled threads && ! enabled pthreads && ! enabled atomics_native && die "non pthread threading without atomics not supported, try adding --enable-pthreads or --cpu=i486 or higher if you are on x86"
# enabled avresample && warn "Building with deprecated library libavresample"

# case $target_os in
# haiku)
#     disable memalign
#     disable posix_memalign
#     ;;
# *-dos|freedos|opendos)
#     if test_cpp_condition sys/version.h "defined(__DJGPP__) && __DJGPP__ == 2 && __DJGPP_MINOR__ == 5"; then
#         disable memalign
#     fi
#     ;;
# esac

# flatten_extralibs(){
#     nested_entries=
#     list_name=$1
#     eval list=\$${1}
#     for entry in $list; do
#         entry_copy=$entry
#         resolve entry_copy
#         flat_entries=
#         for e in $entry_copy; do
#             case $e in
#                 *_extralibs) nested_entries="$nested_entries$e ";;
#                           *) flat_entries="$flat_entries$e ";;
#             esac
#         done
#         eval $entry="\$flat_entries"
#     done
#     append $list_name "$nested_entries"

#     resolve nested_entries
#     if test -n "$(filter '*_extralibs' $nested_entries)"; then
#         flatten_extralibs $list_name
#     fi
# }

# flatten_extralibs_wrapper(){
#     list_name=$1
#     flatten_extralibs $list_name
#     unique $list_name
#     resolve $list_name
#     eval $list_name=\$\(\$ldflags_filter \$$list_name\)
#     eval printf \''%s'\' \""\$$list_name"\"
# }

# for linkunit in $LIBRARY_LIST; do
#     unset current_extralibs
#     eval components=\$$(toupper ${linkunit})_COMPONENTS_LIST
#     for comp in ${components}; do
#         enabled $comp || continue
#         comp_extralibs="${comp}_extralibs"
#         append current_extralibs $comp_extralibs
#     done
#     eval prepend ${linkunit}_extralibs $current_extralibs
# done

# for linkunit in $LIBRARY_LIST $PROGRAM_LIST $EXTRALIBS_LIST; do
#     eval ${linkunit}_extralibs=\$\(flatten_extralibs_wrapper ${linkunit}_extralibs\)
# done

# map 'enabled $v && intrinsics=${v#intrinsics_}' $INTRINSICS_LIST

# for thread in $THREADS_LIST; do
#     if enabled $thread; then
#         test -n "$thread_type" &&
#             die "ERROR: Only one thread type must be selected." ||
#             thread_type="$thread"
#     fi
# done

# if disabled stdatomic; then
#     if enabled atomics_gcc; then
#         add_cppflags '-I\$(SRC_PATH)/compat/atomics/gcc'
#     elif enabled atomics_win32; then
#         add_cppflags '-I\$(SRC_PATH)/compat/atomics/win32'
#     elif enabled atomics_suncc; then
#         add_cppflags '-I\$(SRC_PATH)/compat/atomics/suncc'
#     elif enabled pthreads; then
#         add_compat atomics/pthread/stdatomic.o
#         add_cppflags '-I\$(SRC_PATH)/compat/atomics/pthread'
#     else
#         enabled threads && die "Threading is enabled, but no atomics are available"
#         add_cppflags '-I\$(SRC_PATH)/compat/atomics/dummy'
#     fi
# fi

# # Check if requested libraries were found.
# for lib in $AUTODETECT_LIBS; do
#     requested $lib && ! enabled $lib && die "ERROR: $lib requested but not found";
# done

# enabled zlib && add_cppflags -DZLIB_CONST

# # conditional library dependencies, in any order
# enabled afftdn_filter       && prepend avfilter_deps "avcodec"
# enabled afftfilt_filter     && prepend avfilter_deps "avcodec"
# enabled afir_filter         && prepend avfilter_deps "avcodec"
# enabled amovie_filter       && prepend avfilter_deps "avformat avcodec"
# enabled aresample_filter    && prepend avfilter_deps "swresample"
# enabled atempo_filter       && prepend avfilter_deps "avcodec"
# enabled bm3d_filter         && prepend avfilter_deps "avcodec"
# enabled cover_rect_filter   && prepend avfilter_deps "avformat avcodec"
# enabled convolve_filter     && prepend avfilter_deps "avcodec"
# enabled deconvolve_filter   && prepend avfilter_deps "avcodec"
# enabled ebur128_filter && enabled swresample && prepend avfilter_deps "swresample"
# enabled elbg_filter         && prepend avfilter_deps "avcodec"
# enabled fftfilt_filter      && prepend avfilter_deps "avcodec"
# enabled find_rect_filter    && prepend avfilter_deps "avformat avcodec"
# enabled firequalizer_filter && prepend avfilter_deps "avcodec"
# enabled mcdeint_filter      && prepend avfilter_deps "avcodec"
# enabled movie_filter    && prepend avfilter_deps "avformat avcodec"
# enabled pan_filter          && prepend avfilter_deps "swresample"
# enabled pp_filter           && prepend avfilter_deps "postproc"
# enabled removelogo_filter   && prepend avfilter_deps "avformat avcodec swscale"
# enabled resample_filter && prepend avfilter_deps "avresample"
# enabled sab_filter          && prepend avfilter_deps "swscale"
# enabled scale_filter    && prepend avfilter_deps "swscale"
# enabled scale2ref_filter    && prepend avfilter_deps "swscale"
# enabled sofalizer_filter    && prepend avfilter_deps "avcodec"
# enabled showcqt_filter      && prepend avfilter_deps "avformat avcodec swscale"
# enabled showfreqs_filter    && prepend avfilter_deps "avcodec"
# enabled showspectrum_filter && prepend avfilter_deps "avcodec"
# enabled signature_filter    && prepend avfilter_deps "avcodec avformat"
# enabled smartblur_filter    && prepend avfilter_deps "swscale"
# enabled spectrumsynth_filter && prepend avfilter_deps "avcodec"
# enabled spp_filter          && prepend avfilter_deps "avcodec"
# enabled sr_filter           && prepend avfilter_deps "avformat swscale"
# enabled subtitles_filter    && prepend avfilter_deps "avformat avcodec"
# enabled uspp_filter         && prepend avfilter_deps "avcodec"
# enabled zoompan_filter      && prepend avfilter_deps "swscale"

# enabled lavfi_indev         && prepend avdevice_deps "avfilter"

# #FIXME
# enabled_any sdl2_outdev opengl_outdev && enabled sdl2 &&
#     add_cflags $(filter_out '-Dmain=SDL_main' $sdl2_cflags)

# enabled opus_decoder    && prepend avcodec_deps "swresample"

# # reorder the items at var $1 to align with the items order at var $2 .
# # die if an item at $1 is not at $2 .
# reorder_by(){
#     eval rb_in=\$$1
#     eval rb_ordered=\$$2

#     for rb in $rb_in; do
#         is_in $rb $rb_ordered || die "$rb at \$$1 is not at \$$2"
#     done

#     rb_out=
#     for rb in $rb_ordered; do
#         is_in $rb $rb_in && rb_out="$rb_out$rb "
#     done
#     eval $1=\$rb_out
# }

# # deps-expand fflib $1:  N x {append all expanded deps; unique}
# # within a set of N items, N expansions are enough to expose a cycle.
# expand_deps(){
#     unique ${1}_deps  # required for the early break test.
#     for dummy in $LIBRARY_LIST; do  # N iteratios
#         eval deps=\$${1}_deps
#         append ${1}_deps $(map 'eval echo \$${v}_deps' $deps)
#         unique ${1}_deps
#         eval '[ ${#deps} = ${#'${1}_deps'} ]' && break  # doesn't expand anymore
#     done

#     eval is_in $1 \$${1}_deps && die "Dependency cycle at ${1}_deps"
#     reorder_by ${1}_deps LIBRARY_LIST  # linking order is expected later
# }

# #we have to remove gpl from the deps here as some code assumes all lib deps are libs
# postproc_deps="$(filter_out 'gpl' $postproc_deps)"

# map 'expand_deps $v' $LIBRARY_LIST

# if test "$quiet" != "yes"; then

# echo "install prefix            $prefix"
# echo "source path               $source_path"
# echo "C compiler                $cc"
# echo "C library                 $libc_type"
# if test "$host_cc" != "$cc"; then
#     echo "host C compiler           $host_cc"
#     echo "host C library            $host_libc_type"
# fi
# echo "ARCH                      $arch ($cpu)"
# if test "$build_suffix" != ""; then
#     echo "build suffix              $build_suffix"
# fi
# if test "$progs_suffix" != ""; then
#     echo "progs suffix              $progs_suffix"
# fi
# if test "$extra_version" != ""; then
#     echo "version string suffix     $extra_version"
# fi
# echo "big-endian                ${bigendian-no}"
# echo "runtime cpu detection     ${runtime_cpudetect-no}"
# if enabled x86; then
#     echo "standalone assembly       ${x86asm-no}"
#     echo "x86 assembler             ${x86asmexe}"
#     echo "MMX enabled               ${mmx-no}"
#     echo "MMXEXT enabled            ${mmxext-no}"
#     echo "3DNow! enabled            ${amd3dnow-no}"
#     echo "3DNow! extended enabled   ${amd3dnowext-no}"
#     echo "SSE enabled               ${sse-no}"
#     echo "SSSE3 enabled             ${ssse3-no}"
#     echo "AESNI enabled             ${aesni-no}"
#     echo "AVX enabled               ${avx-no}"
#     echo "AVX2 enabled              ${avx2-no}"
#     echo "AVX-512 enabled           ${avx512-no}"
#     echo "XOP enabled               ${xop-no}"
#     echo "FMA3 enabled              ${fma3-no}"
#     echo "FMA4 enabled              ${fma4-no}"
#     echo "i686 features enabled     ${i686-no}"
#     echo "CMOV is fast              ${fast_cmov-no}"
#     echo "EBX available             ${ebx_available-no}"
#     echo "EBP available             ${ebp_available-no}"
# fi
# if enabled aarch64; then
#     echo "NEON enabled              ${neon-no}"
#     echo "VFP enabled               ${vfp-no}"
# fi
# if enabled arm; then
#     echo "ARMv5TE enabled           ${armv5te-no}"
#     echo "ARMv6 enabled             ${armv6-no}"
#     echo "ARMv6T2 enabled           ${armv6t2-no}"
#     echo "VFP enabled               ${vfp-no}"
#     echo "NEON enabled              ${neon-no}"
#     echo "THUMB enabled             ${thumb-no}"
# fi
# if enabled mips; then
#     echo "MIPS FPU enabled          ${mipsfpu-no}"
#     echo "MIPS DSP R1 enabled       ${mipsdsp-no}"
#     echo "MIPS DSP R2 enabled       ${mipsdspr2-no}"
#     echo "MIPS MSA enabled          ${msa-no}"
#     echo "MIPS MSA2 enabled         ${msa2-no}"
#     echo "LOONGSON MMI enabled      ${mmi-no}"
# fi
# if enabled ppc; then
#     echo "AltiVec enabled           ${altivec-no}"
#     echo "VSX enabled               ${vsx-no}"
#     echo "POWER8 enabled            ${power8-no}"
#     echo "PPC 4xx optimizations     ${ppc4xx-no}"
#     echo "dcbzl available           ${dcbzl-no}"
# fi
# echo "debug symbols             ${debug-no}"
# echo "strip symbols             ${stripping-no}"
# echo "optimize for size         ${small-no}"
# echo "optimizations             ${optimizations-no}"
# echo "static                    ${static-no}"
# echo "shared                    ${shared-no}"
# echo "postprocessing support    ${postproc-no}"
# echo "network support           ${network-no}"
# echo "threading support         ${thread_type-no}"
# echo "safe bitstream reader     ${safe_bitstream_reader-no}"
# echo "texi2html enabled         ${texi2html-no}"
# echo "perl enabled              ${perl-no}"
# echo "pod2man enabled           ${pod2man-no}"
# echo "makeinfo enabled          ${makeinfo-no}"
# echo "makeinfo supports HTML    ${makeinfo_html-no}"
# test -n "$random_seed" &&
#     echo "random seed               ${random_seed}"
# echo

# echo "External libraries:"
# print_enabled '' $EXTERNAL_LIBRARY_LIST $EXTERNAL_AUTODETECT_LIBRARY_LIST | print_in_columns
# echo

# echo "External libraries providing hardware acceleration:"
# print_enabled '' $HWACCEL_LIBRARY_LIST $HWACCEL_AUTODETECT_LIBRARY_LIST | print_in_columns
# echo

# echo "Libraries:"
# print_enabled '' $LIBRARY_LIST | print_in_columns
# echo

# echo "Programs:"
# print_enabled '' $PROGRAM_LIST | print_in_columns
# echo

# for type in decoder encoder hwaccel parser demuxer muxer protocol filter bsf indev outdev; do
#     echo "Enabled ${type}s:"
#     eval list=\$$(toupper $type)_LIST
#     print_enabled '_*' $list | print_in_columns
#     echo
# done

# if test -n "$ignore_tests"; then
#     ignore_tests=$(echo $ignore_tests | tr ',' ' ')
#     echo "Ignored FATE tests:"
#     echo $ignore_tests | print_in_columns
#     echo
# fi

# echo "License: $license"

# fi # test "$quiet" != "yes"

# if test -n "$WARN_IF_GETS_DISABLED_LIST"; then
#     for cfg in $WARN_IF_GETS_DISABLED_LIST; do
#         if disabled $cfg; then
#             varname=${cfg}_disable_reason
#             eval "warn \"Disabled $cfg because \$$varname\""
#         fi
#     done
# fi

# if test -n "$WARNINGS"; then
#     printf "\n%s%s$WARNINGS%s" "$warn_color" "$bold_color" "$reset_color"
#     enabled fatal_warnings && exit 1
# fi

# test -e Makefile || echo "include $source_path/Makefile" > Makefile

# esc(){
#     echo "$*" | sed 's/%/%25/g;s/:/%3a/g'
# }

# echo "config:$arch:$subarch:$cpu:$target_os:$(esc $cc_ident):$(esc $FFMPEG_CONFIGURATION)" > ffbuild/config.fate

# enabled stripping || strip="echo skipping strip"
# enabled stripping || striptype=""

# config_files="$TMPH ffbuild/config.mak doc/config.texi"

# cat > ffbuild/config.mak <<EOF
# # Automatically generated by configure - do not modify!
# ifndef FFMPEG_CONFIG_MAK
# FFMPEG_CONFIG_MAK=1
# FFMPEG_CONFIGURATION=$FFMPEG_CONFIGURATION
# prefix=$prefix
# LIBDIR=\$(DESTDIR)$libdir
# SHLIBDIR=\$(DESTDIR)$shlibdir
# INCDIR=\$(DESTDIR)$incdir
# BINDIR=\$(DESTDIR)$bindir
# DATADIR=\$(DESTDIR)$datadir
# DOCDIR=\$(DESTDIR)$docdir
# MANDIR=\$(DESTDIR)$mandir
# PKGCONFIGDIR=\$(DESTDIR)$pkgconfigdir
# INSTALL_NAME_DIR=$install_name_dir
# SRC_PATH=$source_path
# SRC_LINK=$source_link
# ifndef MAIN_MAKEFILE
# SRC_PATH:=\$(SRC_PATH:.%=..%)
# endif
# CC_IDENT=$cc_ident
# ARCH=$arch
# INTRINSICS=$intrinsics
# EXTERN_PREFIX=$extern_prefix
# CC=$cc
# CXX=$cxx
# AS=$as
# OBJCC=$objcc
# LD=$ld
# DEPCC=$dep_cc
# DEPCCFLAGS=$DEPCCFLAGS \$(CPPFLAGS)
# DEPAS=$as
# DEPASFLAGS=$DEPASFLAGS \$(CPPFLAGS)
# X86ASM=$x86asmexe
# DEPX86ASM=$x86asmexe
# DEPX86ASMFLAGS=\$(X86ASMFLAGS)
# AR=$ar
# ARFLAGS=$arflags
# AR_O=$ar_o
# AR_CMD=$ar
# NM_CMD=$nm
# RANLIB=$ranlib
# STRIP=$strip
# STRIPTYPE=$striptype
# NVCC=$nvcc
# CP=cp -p
# LN_S=$ln_s
# CPPFLAGS=$CPPFLAGS
# CFLAGS=$CFLAGS
# CXXFLAGS=$CXXFLAGS
# OBJCFLAGS=$OBJCFLAGS
# ASFLAGS=$ASFLAGS
# NVCCFLAGS=$nvccflags
# AS_C=$AS_C
# AS_O=$AS_O
# OBJCC_C=$OBJCC_C
# OBJCC_E=$OBJCC_E
# OBJCC_O=$OBJCC_O
# CC_C=$CC_C
# CC_E=$CC_E
# CC_O=$CC_O
# CXX_C=$CXX_C
# CXX_O=$CXX_O
# NVCC_C=$NVCC_C
# NVCC_O=$NVCC_O
# LD_O=$LD_O
# X86ASM_O=$X86ASM_O
# LD_LIB=$LD_LIB
# LD_PATH=$LD_PATH
# DLLTOOL=$dlltool
# WINDRES=$windres
# DEPWINDRES=$dep_cc
# DOXYGEN=$doxygen
# LDFLAGS=$LDFLAGS
# LDEXEFLAGS=$LDEXEFLAGS
# LDSOFLAGS=$LDSOFLAGS
# SHFLAGS=$(echo $($ldflags_filter $SHFLAGS))
# ASMSTRIPFLAGS=$ASMSTRIPFLAGS
# X86ASMFLAGS=$X86ASMFLAGS
# BUILDSUF=$build_suffix
# PROGSSUF=$progs_suffix
# FULLNAME=$FULLNAME
# LIBPREF=$LIBPREF
# LIBSUF=$LIBSUF
# LIBNAME=$LIBNAME
# SLIBPREF=$SLIBPREF
# SLIBSUF=$SLIBSUF
# EXESUF=$EXESUF
# EXTRA_VERSION=$extra_version
# CCDEP=$CCDEP
# CXXDEP=$CXXDEP
# CCDEP_FLAGS=$CCDEP_FLAGS
# ASDEP=$ASDEP
# ASDEP_FLAGS=$ASDEP_FLAGS
# X86ASMDEP=$X86ASMDEP
# X86ASMDEP_FLAGS=$X86ASMDEP_FLAGS
# CC_DEPFLAGS=$CC_DEPFLAGS
# AS_DEPFLAGS=$AS_DEPFLAGS
# X86ASM_DEPFLAGS=$X86ASM_DEPFLAGS
# HOSTCC=$host_cc
# HOSTLD=$host_ld
# HOSTCFLAGS=$host_cflags
# HOSTCPPFLAGS=$host_cppflags
# HOSTEXESUF=$HOSTEXESUF
# HOSTLDFLAGS=$host_ldflags
# HOSTEXTRALIBS=$host_extralibs
# DEPHOSTCC=$host_cc
# DEPHOSTCCFLAGS=$DEPHOSTCCFLAGS \$(HOSTCCFLAGS)
# HOSTCCDEP=$HOSTCCDEP
# HOSTCCDEP_FLAGS=$HOSTCCDEP_FLAGS
# HOSTCC_DEPFLAGS=$HOSTCC_DEPFLAGS
# HOSTCC_C=$HOSTCC_C
# HOSTCC_O=$HOSTCC_O
# HOSTLD_O=$HOSTLD_O
# TARGET_EXEC=$target_exec $target_exec_args
# TARGET_PATH=$target_path
# TARGET_SAMPLES=${target_samples:-\$(SAMPLES)}
# CFLAGS-ffplay=${sdl2_cflags}
# CFLAGS_HEADERS=$CFLAGS_HEADERS
# LIB_INSTALL_EXTRA_CMD=$LIB_INSTALL_EXTRA_CMD
# EXTRALIBS=$extralibs
# COMPAT_OBJS=$compat_objs
# INSTALL=$install
# LIBTARGET=${LIBTARGET}
# SLIBNAME=${SLIBNAME}
# SLIBNAME_WITH_VERSION=${SLIBNAME_WITH_VERSION}
# SLIBNAME_WITH_MAJOR=${SLIBNAME_WITH_MAJOR}
# SLIB_CREATE_DEF_CMD=${SLIB_CREATE_DEF_CMD}
# SLIB_EXTRA_CMD=${SLIB_EXTRA_CMD}
# SLIB_INSTALL_NAME=${SLIB_INSTALL_NAME}
# SLIB_INSTALL_LINKS=${SLIB_INSTALL_LINKS}
# SLIB_INSTALL_EXTRA_LIB=${SLIB_INSTALL_EXTRA_LIB}
# SLIB_INSTALL_EXTRA_SHLIB=${SLIB_INSTALL_EXTRA_SHLIB}
# VERSION_SCRIPT_POSTPROCESS_CMD=${VERSION_SCRIPT_POSTPROCESS_CMD}
# SAMPLES:=${samples:-\$(FATE_SAMPLES)}
# NOREDZONE_FLAGS=$noredzone_flags
# LIBFUZZER_PATH=$libfuzzer_path
# IGNORE_TESTS=$ignore_tests
# EOF

# map 'eval echo "${v}_FFLIBS=\$${v}_deps" >> ffbuild/config.mak' $LIBRARY_LIST

# for entry in $LIBRARY_LIST $PROGRAM_LIST $EXTRALIBS_LIST; do
#     eval echo "EXTRALIBS-${entry}=\$${entry}_extralibs" >> ffbuild/config.mak
# done

# cat > $TMPH <<EOF
# /* Automatically generated by configure - do not modify! */
# #ifndef FFMPEG_CONFIG_H
# #define FFMPEG_CONFIG_H
# #define FFMPEG_CONFIGURATION "$(c_escape $FFMPEG_CONFIGURATION)"
# #define FFMPEG_LICENSE "$(c_escape $license)"
# #define CONFIG_THIS_YEAR 2019
# #define FFMPEG_DATADIR "$(eval c_escape $datadir)"
# #define AVCONV_DATADIR "$(eval c_escape $datadir)"
# #define CC_IDENT "$(c_escape ${cc_ident:-Unknown compiler})"
# #define av_restrict $restrict_keyword
# #define EXTERN_PREFIX "${extern_prefix}"
# #define EXTERN_ASM ${extern_prefix}
# #define BUILDSUF "$build_suffix"
# #define SLIBSUF "$SLIBSUF"
# #define HAVE_MMX2 HAVE_MMXEXT
# #define SWS_MAX_FILTER_SIZE $sws_max_filter_size
# EOF

# test -n "$assert_level" &&
#     echo "#define ASSERT_LEVEL $assert_level" >>$TMPH

# test -n "$malloc_prefix" &&
#     echo "#define MALLOC_PREFIX $malloc_prefix" >>$TMPH

# if enabled x86asm; then
#     append config_files $TMPASM
#     cat > $TMPASM <<EOF
# ; Automatically generated by configure - do not modify!
# EOF
# fi

# enabled getenv || echo "#define getenv(x) NULL" >> $TMPH


# mkdir -p doc
# mkdir -p tests
# mkdir -p tests/api
# echo "@c auto-generated by configure - do not modify! " > doc/config.texi

# print_config ARCH_   "$config_files" $ARCH_LIST
# print_config HAVE_   "$config_files" $HAVE_LIST
# print_config CONFIG_ "$config_files" $CONFIG_LIST       \
#                                      $CONFIG_EXTRA      \
#                                      $ALL_COMPONENTS    \

# echo "#endif /* FFMPEG_CONFIG_H */" >> $TMPH
# echo "endif # FFMPEG_CONFIG_MAK" >> ffbuild/config.mak

# # Do not overwrite an unchanged config.h to avoid superfluous rebuilds.
# cp_if_changed $TMPH config.h
# touch ffbuild/.config

# enabled x86asm && cp_if_changed $TMPASM config.asm

# cat > $TMPH <<EOF
# /* Generated by ffmpeg configure */
# #ifndef AVUTIL_AVCONFIG_H
# #define AVUTIL_AVCONFIG_H
# EOF

# print_config AV_HAVE_ $TMPH $HAVE_LIST_PUB

# echo "#endif /* AVUTIL_AVCONFIG_H */" >> $TMPH

# cp_if_changed $TMPH libavutil/avconfig.h

# # full_filter_name_foo=vf_foo
# # full_filter_name_bar=asrc_bar
# # ...
# eval "$(sed -n "s/^extern AVFilter ff_\([avfsinkrc]\{2,5\}\)_\(.*\);/full_filter_name_\2=\1_\2/p" $source_path/libavfilter/allfilters.c)"

# # generate the lists of enabled components
# print_enabled_components(){
#     file=$1
#     struct_name=$2
#     name=$3
#     shift 3
#     echo "static const $struct_name * const $name[] = {" > $TMPH
#     for c in $*; do
#         if enabled $c; then
#             case $name in
#                 filter_list)
#                     eval c=\$full_filter_name_${c%_filter}
#                 ;;
#                 indev_list)
#                     c=${c%_indev}_demuxer
#                 ;;
#                 outdev_list)
#                     c=${c%_outdev}_muxer
#                 ;;
#             esac
#             printf "    &ff_%s,\n" $c >> $TMPH
#         fi
#     done
#     if [ "$name" = "filter_list" ]; then
#         for c in asrc_abuffer vsrc_buffer asink_abuffer vsink_buffer; do
#             printf "    &ff_%s,\n" $c >> $TMPH
#         done
#     fi
#     echo "    NULL };" >> $TMPH
#     cp_if_changed $TMPH $file
# }

# print_enabled_components libavfilter/filter_list.c AVFilter filter_list $FILTER_LIST
# print_enabled_components libavcodec/codec_list.c AVCodec codec_list $CODEC_LIST
# print_enabled_components libavcodec/parser_list.c AVCodecParser parser_list $PARSER_LIST
# print_enabled_components libavcodec/bsf_list.c AVBitStreamFilter bitstream_filters $BSF_LIST
# print_enabled_components libavformat/demuxer_list.c AVInputFormat demuxer_list $DEMUXER_LIST
# print_enabled_components libavformat/muxer_list.c AVOutputFormat muxer_list $MUXER_LIST
# print_enabled_components libavdevice/indev_list.c AVInputFormat indev_list $INDEV_LIST
# print_enabled_components libavdevice/outdev_list.c AVOutputFormat outdev_list $OUTDEV_LIST
# print_enabled_components libavformat/protocol_list.c URLProtocol url_protocols $PROTOCOL_LIST

# # Settings for pkg-config files

# cat > $TMPH <<EOF
# # Automatically generated by configure - do not modify!
# shared=$shared
# build_suffix=$build_suffix
# prefix=$prefix
# libdir=$libdir
# incdir=$incdir
# rpath=$(enabled rpath && echo "-Wl,-rpath,\${libdir}")
# source_path=${source_path}
# LIBPREF=${LIBPREF}
# LIBSUF=${LIBSUF}
# extralibs_avutil="$avutil_extralibs"
# extralibs_avcodec="$avcodec_extralibs"
# extralibs_avformat="$avformat_extralibs"
# extralibs_avdevice="$avdevice_extralibs"
# extralibs_avfilter="$avfilter_extralibs"
# extralibs_avresample="$avresample_extralibs"
# extralibs_postproc="$postproc_extralibs"
# extralibs_swscale="$swscale_extralibs"
# extralibs_swresample="$swresample_extralibs"
# EOF

# for lib in $LIBRARY_LIST; do
#     lib_deps="$(eval echo \$${lib}_deps)"
#     echo ${lib}_deps=\"$lib_deps\" >> $TMPH
# done

# cp_if_changed $TMPH ffbuild/config.sh
