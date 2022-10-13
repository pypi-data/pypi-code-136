#!/usr/bin/python3
# region data
import io
import os
import re
import ast
import sys
import hashlib
import logging
import random
import asyncio
import datetime
import mimetypes
import sqlite3
import httplib2

from PIL import Image
from loguru import logger
from random import randrange
from contextlib import closing
import moviepy.editor as mp
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials

from telegraph import Telegraph
from pyrogram import enums, Client
from pyrogram.raw import functions
from pyrogram.errors import FloodWait, UserAlreadyParticipant, UsernameInvalid, BadRequest, SlowmodeWait, \
    UserDeactivatedBan, SessionRevoked, SessionExpired, AuthKeyUnregistered, AuthKeyInvalid, AuthKeyDuplicated, \
    InviteHashExpired, InviteHashInvalid, ChatAdminRequired, UserDeactivated, UsernameNotOccupied, ChannelBanned
from aiogram import types
from aiogram.types import ChatActions
from aiogram.utils.exceptions import RetryAfter, MessageNotModified, MessageIdInvalid, MessageToEditNotFound

one_minute = 60
one_hour = 3600
my_tid = 5491025132
old_tid = 4_000_000_000
lat_company = 59.395881
long_company = 24.658980
lkjhgfdsa_channel = -1001657854832

SECTION = 'CONFIG'
short_name = 'me'
const_url = 'https://t.me/'
phone_number = '79999999999'
vk_group = 'https://vk.com'
vk_account = 'https://vk.com'
website = 'https://google.com'
facebook = 'https://www.facebook.com'
telegram_account = 'https://t.me'
ferey_telegram_username = 'ferey_support'
ferey_telegram_demo_bot = 'ferey_demo_bot'
ferey_telegram_group = 'ferey_group_europe'
ferey_telegram_channel = 'ferey_channel_europe'
ferey_instagram = 'https://www.instagram.com/ferey.chatbot'
ferey_address = "Estônia, Tāllin, Mäepealse, 2/1"
ferey_title = "Ferey Inc."
payment_link = 'http://bagazhznaniy.ru/wp-content/uploads/2014/03/zhivaya-priroda.jpg'
whatsup = f'https://api.whatsapp.com/send?phone={phone_number}&text=%D0%94%D0%BE%D0%B1%D1%80%D1%8B%D0%B9%20%D0%B4%D0%B5%D0%BD%D1%8C%2C%20%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D0%B2%D0%BE%D0%B4%D1%83%20%D0%92%D0%B0%D1%88%D0%B5%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0!'


# endregion


# region db
def sqlite_lower(value_):
    return value_.lower() if value_ else None


def sqlite_upper(value_):
    return value_.upper() if value_ else None


def ignore_case_collation(value1_, value2_):
    if value1_ is None or value2_ is None:
        return 1
    if value1_.lower() == value2_.lower():
        return 0
    elif value1_.lower() < value2_.lower():
        return -1
    else:
        return 1


async def dbSELECT(sql, param=None, db=None):
    retry = 2
    while retry > 0:
        try:
            with closing(sqlite3.connect(db, timeout=15)) as con:
                con.execute('PRAGMA foreign_keys=ON;')
                # con.create_collation("NOCASE", ignore_case_collation)
                # con.create_function("LOWER", 1, sqlite_lower)
                # con.create_function("UPPER", 1, sqlite_upper)
                with closing(con.cursor()) as cur:
                    if param:
                        cur.execute(sql, param)
                    else:
                        cur.execute(sql)

                    return cur.fetchall()
        except Exception as e:
            logger.info(f'\033[{92}m%s\033[0m' % str(e))
            await asyncio.sleep(round(random.uniform(1, 2), 2))
            retry -= 1
    return []


async def dbCHANGE(sql, param=None, db=None):
    retry = 2
    while retry > 0:
        try:
            with closing(sqlite3.connect(db, timeout=15)) as con:
                con.execute('PRAGMA foreign_keys=ON;')
                with closing(con.cursor()) as cur:
                    if param:
                        cur.execute(sql, param)
                    else:
                        cur.execute(sql)

                    con.commit()
                    return cur.lastrowid
        except Exception as e:
            logger.info(f'\033[{92}m%s\033[0m' % str(e))
            await asyncio.sleep(round(random.uniform(1, 2), 2))
            retry -= 1
    return 0


# endregion


# region sender
async def autoDestroyMsg(bot, telegram_bot, chat_id, text, message_id, type_='text', sec=5):
    result = None
    try:
        step = 1
        by = f"<a href='https://t.me/{ferey_telegram_demo_bot}'>by</a>"
        text = f"{text}\n\n{by} @{telegram_bot} <b>{sec}</b>sec"
        ix_sec = text.rfind('</b>sec')
        while text[ix_sec] != '>': ix_sec -= 1

        while sec > 0:
            try:
                text = text.replace(f"<b>{sec}</b>sec", f"<b>{sec - 1}</b>sec")
                sec -= step
                if type_ == 'text':
                    await bot.edit_message_text(chat_id=chat_id, text=text, message_id=message_id, disable_web_page_preview=True)
                else:
                    await bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption=text)
                await asyncio.sleep(1)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                await asyncio.sleep(round(random.uniform(1, 2), 2))
                break
        await bot.delete_message(chat_id, message_id)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyText(bot, chat_id, text, reply_markup=None, disable_web_page_preview=True, typetime=None):
    result = None
    try:
        # печатает
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.TYPING)

        text = await noWarText(text)
        text = text[0:4095]

        if typetime:
            copy_text = text
            copy_text = re.sub(re.compile('<.*?>'), '', copy_text)
            copy_text_clean = copy_text
            tbp = ""
            typing_symbol = "▒"
            result = await bot.send_message(chat_id=chat_id, text=copy_text, reply_markup=reply_markup)
            couple = int(len(copy_text) / 99) + 3

            for i in range(0, 99):
                try:
                    result = await bot.edit_message_text(text=tbp + typing_symbol, chat_id=chat_id,
                                                         message_id=result.message_id, reply_markup=reply_markup)
                    await asyncio.sleep(0.07)

                    tbp = tbp + copy_text[0:couple]
                    copy_text = copy_text[couple:]

                    result = await bot.edit_message_text(text=tbp, chat_id=chat_id, message_id=result.message_id,
                                                         reply_markup=reply_markup)
                    await asyncio.sleep(0.07)

                    if copy_text_clean == tbp:
                        break
                except RetryAfter as e:
                    logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
                    await asyncio.sleep(e.timeout)
                except Exception as e:
                    logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                    await asyncio.sleep(round(random.uniform(1, 2), 2))
            # await asyncio.sleep(2)
            await bot.edit_message_text(text=text, chat_id=chat_id, message_id=result.message_id,
                                        reply_markup=reply_markup,
                                        disable_web_page_preview=disable_web_page_preview)
        else:
            result = await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup,
                                            disable_web_page_preview=disable_web_page_preview,
                                            disable_notification=True)
            text = text[0:32].replace('\n', '')
            logger.info(
                f'\033[{92}m%s\033[0m' % f"@{(await bot.get_chat(chat_id)).username} (<code>{chat_id}</code>): {text}")
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyPhoto(bot, chat_id, photo_name, caption, CONF_P, EXTRA_D, MEDIA_D, BASE_D, reply_markup=None,
                      reWrite=True):
    result = None
    try:
        # печатает
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.TYPING)  # UPLOAD_PHOTO

        caption = await noWarText(caption)
        caption = caption[0:1023]
        fl_photo = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, photo_name, reWrite)
        photo = types.InputFile(fl_photo) if fl_photo and '/' in fl_photo and '://' not in fl_photo else fl_photo
        result = await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=reply_markup,
                                      disable_notification=True)
        await safeFileId(result, photo_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyVideo(bot, chat_id, video_name, caption, CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name=None,
                      reply_markup=None, reWrite=True):
    result = None
    try:
        # записывает видео
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_VIDEO)  # RECORD_VIDEO doesn't work

        caption = await noWarText(caption)
        caption = caption[0:1023]

        fl_video = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, video_name, reWrite)
        video = types.InputFile(fl_video) if fl_video and '/' in fl_video else fl_video
        fl_thumb = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name, reWrite, 160)
        thumb = types.InputFile(fl_thumb) if fl_thumb and '/' in fl_thumb else fl_thumb
        result = await bot.send_video(chat_id=chat_id, video=video, thumb=thumb, caption=caption,
                                      reply_markup=reply_markup, disable_notification=True)
        await safeFileId(result, video_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyVideoNote(bot, chat_id, videonote_name, CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name=None,
                          reply_markup=None, reWrite=True):
    result = None
    try:
        # записывает видео # UPLOAD_VIDEO_NOTE - это печатает
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.RECORD_VIDEO_NOTE)

        fl_videonote = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, videonote_name, reWrite, 440)
        videonote = types.InputFile(fl_videonote) if fl_videonote and '/' in fl_videonote else fl_videonote
        fl_thumb = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name, reWrite, 160)
        thumb = types.InputFile(fl_thumb) if fl_thumb and '/' in fl_thumb else fl_thumb
        result = await bot.send_video_note(chat_id=chat_id, video_note=videonote, thumb=thumb,
                                           reply_markup=reply_markup, disable_notification=True)
        await safeFileId(result, videonote_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyMEDIA(bot, chat_id, media_names, CONF_P, EXTRA_D, MEDIA_D, BASE_D, reWrite=True):
    result = None
    try:
        # печатает
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_VIDEO)
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_PHOTO)

        media = types.MediaGroup()
        for media_name in media_names:
            fl_media = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, media_name, reWrite)
            tmp_media = types.InputFile(fl_media) if fl_media and '/' in fl_media else fl_media
            media.attach_photo(tmp_media)

        result = await bot.send_media_group(chat_id=chat_id, media=media, disable_notification=True)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyDoc(bot, chat_id, doc_name, CONF_P, BASE_D, MEDIA_D, EXTRA_D, caption, thumb_name=None,
                    reply_markup=None, reWrite=True):
    # загружает документ
    # thumb - JPEG format,  less than 200 kB in size. A thumbnail‘s width and height should not exceed 320
    result = None
    try:
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_DOCUMENT)

        caption = await noWarText(caption)
        caption = caption[0:1023]

        fl_doc = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, doc_name, reWrite)
        # fl_doc = os.path.abspath(os.path.join(os.path.dirname(__file__),'config.ini'))
        document = types.InputFile(fl_doc) if fl_doc and '/' in fl_doc else fl_doc
        fl_thumb = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name, reWrite, 160)
        thumb = types.InputFile(fl_thumb) if fl_thumb and '/' in fl_thumb else fl_thumb
        result = await bot.send_document(chat_id=chat_id, document=document, thumb=thumb, caption=caption,
                                         reply_markup=reply_markup, disable_notification=True)
        await safeFileId(result, doc_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyAudio(bot, chat_id, audio_name, caption, CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name=None,
                      reply_markup=None, reWrite=True):
    result = None
    try:
        # записывает голосовое сообщение    # = RECORD_AUDIO = UPLOAD_VOICE = RECORD_VOICE
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_AUDIO)

        caption = await noWarText(caption)
        caption = caption[0:1023]

        fl_audio = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, audio_name, reWrite)
        audio = types.InputFile(fl_audio) if fl_audio and '/' in fl_audio else fl_audio
        fl_thumb = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name, reWrite, 160)
        thumb = types.InputFile(fl_thumb) if fl_thumb and '/' in fl_thumb else fl_thumb
        # thumb = types.InputFile(os.path.join(DEFAULT_EXTRA, 'img.png'))
        # title='Canto Ostinato Pt1 Section14.mp3', performer='Simeon ten Holt',
        result = await bot.send_audio(chat_id=chat_id, audio=audio, thumb=thumb, caption=caption, title='Listen',
                                      reply_markup=reply_markup, disable_notification=True)
        await safeFileId(result, audio_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyVoice(bot, chat_id, voice_name, caption, CONF_P, EXTRA_D, MEDIA_D, BASE_D, reply_markup=None,
                      reWrite=True):
    result = None
    try:
        # записывает аудио  # = RECORD_AUDIO = UPLOAD_VOICE = RECORD_VOICE
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_AUDIO)

        caption = await noWarText(caption)
        caption = caption[0:1023]

        fl_voice = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, voice_name, reWrite)
        voice = types.InputFile(fl_voice) if fl_voice and '/' in fl_voice else fl_voice
        result = await bot.send_voice(chat_id=chat_id, voice=voice, caption=caption, reply_markup=reply_markup,
                                      disable_notification=True)
        await safeFileId(result, voice_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyAnimation(bot, chat_id, animation_name, caption, CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name=None,
                          reply_markup=None, reWrite=True):
    result = None
    try:
        # печатает
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.TYPING)  # UPLOAD_PHOTO

        caption = await noWarText(caption)
        caption = caption[0:1023]

        fl_animation = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, animation_name, reWrite)
        animation = types.InputFile(fl_animation) if fl_animation and '/' in fl_animation else fl_animation
        fl_thumb = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, thumb_name, reWrite, 160)
        thumb = types.InputFile(fl_thumb) if fl_thumb and '/' in fl_thumb else fl_thumb
        result = await bot.send_animation(chat_id=chat_id, animation=animation, thumb=thumb, caption=caption,
                                          reply_markup=reply_markup, disable_notification=True)
        await safeFileId(result, animation_name, BASE_D)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMySticker(bot, chat_id, sticker, reply_markup=None):
    result = None
    try:
        # ищет стикер
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.CHOOSE_STICKER)

        result = await bot.send_sticker(chat_id=chat_id, sticker=sticker, reply_markup=reply_markup,
                                        disable_notification=True)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendMyPoll(bot, chat_id, question, options, type_poll=types.PollType.QUIZ, reply_markup=None):
    result = None
    try:
        # печатает
        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.TYPING)

        question = await noWarText(question)
        if isinstance(type_poll, types.PollType.REGULAR):
            result = await bot.send_poll(chat_id=chat_id, is_anonymous=False, type=types.PollType.REGULAR,
                                         allows_multiple_answers=True, reply_markup=reply_markup,
                                         question=question, options=options, disable_notification=True)
        elif isinstance(type_poll, types.PollType.QUIZ):
            result = await bot.send_poll(chat_id, is_anonymous=False, type=types.PollType.QUIZ,
                                         allows_multiple_answers=False, reply_markup=reply_markup,
                                         correct_option_id=0,
                                         explanation=await noWarText('Все верно! Записывайся на консультацию!'),
                                         open_period=30,
                                         question=question, options=options, disable_notification=True)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f'RetryAfter {e.timeout}')
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
        return result


# endregion


# region functions
async def log_old(txt, LOG_DEFAULT, colour=92):
    try:
        logging.info(f'\033[{colour}m%s\033[0m' % (str(txt)))
        with open(LOG_DEFAULT, 'a') as f:
            f.write(str(txt) + '\n')
    except Exception as e:
        logger.info(f'\033[{95}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))


async def log(txt, color=92):
    try:
        '''DESC
21 - underscore     !
30 - black          !
91 - grey
91 - red            !
92 - green          !
93 - yellow         
94 - blue
95 - purple         !
96 - cyan           !
97 - white
---------------------
100 - grey bg
101 - red bg
102 - green bg
103 - yellow bg
104 - blue bg
105 - purple bg
106 - cyan bg
107 - white bg
'''
        logger.info(f'\033[{color}m%s\033[0m' % str(txt))
    except Exception as e:
        logger.info(f'\033[95m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))


async def lz_code(chat_id, lan, BASE_D):
    result = 'en'
    try:
        sql = "SELECT USER_LANG FROM USER WHERE USER_TID=?"
        data = await dbSELECT(sql, (chat_id,), BASE_D)

        # first enter before DB
        if not len(data) or not data[0][0]:
            # chinese
            if lan in ['zh', 'zh-chs', 'zh-cht', 'ja', 'ko', 'zh-CN', 'zh-TW', 'th', 'vi', 'tw', 'sg']:
                result = 'zh'
            # arabic    # ir, af
            elif lan in ['ar-XA', 'ar', 'tr', 'ur', 'fa', 'tj', 'dz', 'eg', 'iq', 'sy', 'ae', 'sa', 'tn', 'ir', 'af']:
                result = 'ar'
            # spanish   # portugal: 'pt', 'br', 'ao', 'mz'
            elif lan in ['es', 'ar', 'cl', 'co', 'cu', 've', 'bo', 'pe', 'ec', 'pt', 'br', 'ao', 'mz']:
                result = 'es'
            # french
            elif lan in ['fr', 'ch', 'be', 'ca']:
                result = 'fr'
            # europe
            elif lan in ['ru', 'kz', 'kg', 'uz', 'tm', 'md', 'am', 'uk-UA', 'uk', 'kk', 'tk', 'ky']:
                result = 'ru'

            sql = "UPDATE USER SET USER_LANG=? WHERE USER_TID=?"
            await dbCHANGE(sql, (result, chat_id,), BASE_D)
        else:
            result = data[0][0]
    except Exception as e:
        logger.info(f'\033[{95}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def noWarText(txt):
    result = txt
    try:
        pass
        # result = txt.replace('а', 'ä').replace('А', 'Ä').replace('в', 'ʙ').replace('В', 'B').replace('г', 'ґ').replace('Г', 'Ґ').replace('е', 'é').replace('Е', 'É').replace('ж', 'җ').replace('Ж', 'Җ').replace('з', 'з́').replace('З', 'З́').replace('й', 'ҋ').replace('Й', 'Ҋ').replace('к','қ').replace('К', 'Қ').replace('М', 'M').replace('Н','H').replace('о', 'ô').replace('О', 'Ô').replace('р', 'p').replace('Р', 'P').replace('с', 'č').replace('С', 'Č').replace('т', 'ҭ').replace('Т', 'Ҭ').replace('у', 'ў').replace('У', 'Ў').replace('х', 'x').replace('Х', 'X').replace('э', 'є').replace('Э', 'Є')
        # result = txt.replace('А', 'Ä').replace('в', 'ʙ').replace('В', 'B').replace('г', 'ґ').replace('Г', 'Ґ').replace(
        #     'Е', 'É').replace('ж', 'җ').replace('Ж', 'Җ').replace('й', 'ҋ').replace('К', 'Қ').replace('М', 'M').replace(
        #     'Н', 'H').replace('о', 'ô').replace('О', 'Ô').replace('р', 'p').replace('Р', 'P').replace('С', 'Č').replace(
        #     'Т', 'Ҭ').replace('У', 'Ў').replace('х', 'x').replace('Х', 'X').replace('э', 'є')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


async def getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, src, reWrite=False, basewidth=1024):
    result = None
    try:
        isLink = await isUrl(src)
        file_id = await getFileIdBySrc(src, isLink, BASE_D)
        if isLink and 'drive.google.com' not in src:
            result = src
        elif src is None:
            result = None
        elif file_id and reWrite is False:
            result = file_id
        else:
            if os.path.basename(src) in os.listdir(MEDIA_D) and reWrite is False:
                result = os.path.abspath(os.path.join(MEDIA_D, os.path.basename(src)))
            else:
                scopes = rConf('scopes', CONF_P)
                credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
                credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
                httpAuth = credentials.authorize(httplib2.Http())
                drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)

                if isLink:
                    docid = getDocIdFromLink(src)
                    file_list_dic = await apiGetFileList(drive_service, docid, {}, isFile=True)
                else:
                    file_list_dic = await apiGetFileList(drive_service, (rConf('share_folder_id', CONF_P))[0], {})

                for k, v in file_list_dic.items():
                    if isLink:
                        result = await apiDlFile(drive_service, k, v[0], v[1], MEDIA_D)
                        break
                    elif str(v[0]).lower() == str(os.path.basename(src)).lower():
                        result = await apiDlFile(drive_service, k, v[0], v[1], MEDIA_D)
                        break

            if await isImage(result):
                result = await resizeMedia(result, basewidth)
            elif await isVideo(result):
                result = await resizeVideoNote(result, basewidth)
            logger.info(f'\033[{92}m%s\033[0m' % 'dl media ok')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


async def isUrl(url):
    status = False
    try:
        if url and '://' in url:  # and requests.get(url).status_code == 200:
            status = True
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return status


async def getFileIdBySrc(src, isLink, BASE_D):
    data = None
    try:
        if isLink:
            sql = "SELECT FILE_FILEID FROM FILE WHERE FILE_FILELINK = ?"
        else:
            sql = "SELECT FILE_FILEID FROM FILE WHERE FILE_FILENAME = ?"
        data = await dbSELECT(sql, (src,), BASE_D)
        if not data:
            return None
        data = data[0][0]
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return data


async def isImage(file_name):
    im = None
    try:
        if str(file_name).lower().endswith('.docx') or str(file_name).lower().endswith('.pdf') or str(
                file_name).lower().endswith('.mp4'):
            return False
        im = Image.open(file_name)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % 'isImage: ' + str(e))
    finally:
        return im


async def isVideo(file_name):
    vi = None
    try:
        vi = True if str(mimetypes.guess_type(file_name)[0]).startswith('video') else False
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % 'isVideo: ' + str(e))
    finally:
        return vi


async def resizeMedia(file_name, basewidth=1024):
    result = file_name
    try:
        if str(file_name).lower().endswith('.png'):
            im = Image.open(file_name)
            rgb_im = im.convert('RGB')
            tmp_name = os.path.join(os.path.dirname(file_name), getNameWithoutExt(file_name) + '.jpg')
            rgb_im.save(tmp_name)
            if os.path.exists(file_name):
                os.remove(file_name)
            result = file_name = tmp_name

        img = Image.open(file_name)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.LANCZOS)
        img.save(file_name)
        result = file_name
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


async def resizeVideoNote(file_name, basewidth):
    result = file_name
    try:
        if not str(file_name).lower().endswith('.mp4'):
            clip = mp.VideoFileClip(file_name)
            tmp_name = os.path.join(os.path.dirname(file_name), 'r_' + os.path.basename(file_name))
            clip.write_videofile(tmp_name, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a',
                                 remove_temp=True)

            if os.path.exists(file_name):
                os.remove(file_name)
            file_name = os.path.join(os.path.dirname(file_name), getNameWithoutExt(file_name) + '.mp4')
            if os.path.exists(tmp_name):
                os.rename(tmp_name, file_name)
            result = file_name
        if basewidth == 440:
            clip = mp.VideoFileClip(file_name)
            clip_resized = clip.resize((basewidth, basewidth))
            tmp_name = os.path.join(os.path.dirname(file_name), 'r_' + os.path.basename(file_name))
            clip_resized.write_videofile(tmp_name, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a',
                                         remove_temp=True)
            if os.path.exists(file_name):
                os.remove(file_name)
            if os.path.exists(tmp_name):
                os.rename(tmp_name, file_name)
            result = file_name
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


async def getThumbnail(MEDIA_D, file_name, sz_thumbnail=32):
    from PIL import Image
    size = sz_thumbnail, sz_thumbnail
    result = ''
    try:
        name = getNameWithoutExt(file_name)
        im = Image.open(file_name)
        im.thumbnail(size, Image.ANTIALIAS)
        result = f'{MEDIA_D}/"thumbnail_"{name}'
        im.save(result, "JPEG")
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


def touch(path):
    if not os.path.exists(path):
        with open(path, 'a'):
            os.utime(path, None)


def getNumbersWithMark(data, id_, row_width=5):
    btns = []
    middle = int(row_width / 2 + 1)
    length = 5 if len(data) < 5 else len(data)

    if id_ == 1 or id_ == 2 or id_ == 3:
        btns.insert(0, f'1')
        btns.insert(1, f'2')
        btns.insert(2, f'3')
        btns.insert(3, f'4›')
        btns.insert(4, f'{length}»')

        btns[id_ - 1] = f'· {id_} ·'
    elif middle < id_ < length - middle + 1:  # 4
        btns.insert(0, f'«1')
        btns.insert(1, f'‹{id_ - 1}')
        btns.insert(2, f'· {id_} ·')
        btns.insert(3, f'{id_ + 1}›')
        btns.insert(4, f'{length}»')
    elif id_ == length or id_ == length - 1 or id_ == length - 2:
        btns.insert(0, f'«1')
        btns.insert(1, f'‹{length - 3}')
        btns.insert(2, f'{length - 2}')
        btns.insert(3, f'{length - 1}')
        btns.insert(4, f'{length}')

        btns[(row_width - (length - id_)) - 1] = f'· {id_} ·'

    if id_ == 4 and len(data) == 4:
        btns = ['«1', '‹2', '3', '· 4 ·', '5']

    return btns


def get_keyboard(data, src, POST_ID=1, group_id=''):
    row_width = len(data) if len(data) < 5 else 5
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    btns = getNumbersWithMark(data, POST_ID, row_width)
    buttons = []

    for i in range(1, row_width + 1):
        arr = re.split('\s|[«‹·›»]', btns[i - 1])  # ('\s|(?<!\d)[,.](?!\d)', s)
        page_i = list(filter(None, arr))[0]
        page_name = f'page_{src}_{group_id}_{str(int(page_i))}'
        buttons.append(types.InlineKeyboardButton(text=btns[i - 1], callback_data=page_name))
    keyboard.add(*buttons)

    return keyboard


async def safeFileId(message, src, BASE_D):
    if message is None: return
    file_id = usr_id = ''
    if message.photo:
        file_id = message.photo[-1].file_id
    elif message.animation:  # giff
        file_id = message.animation.file_id
    elif message.video:
        file_id = message.video.file_id
    elif message.audio:  # m4a
        file_id = message.audio.file_id
    elif message.voice:
        file_id = message.voice.file_id
    elif message.video_note:
        file_id = message.video_note.file_id
    elif message.document:
        file_id = message.document.file_id
    elif message.poll:
        file_id = message.poll.id

    if await isUrl(src):
        sql = f"INSERT OR IGNORE INTO FILE (FILE_FILEID, FILE_FILELINK) VALUES (?, ?);"
    else:
        sql = "INSERT OR IGNORE INTO FILE (FILE_FILEID, FILE_FILENAME) VALUES (?, ?);"
    if not await isExistsFILENAMEorFILELINK(src, BASE_D):
        usr_id = await dbCHANGE(sql, (file_id, src,), BASE_D)
    return usr_id


async def isExistsFILENAMEorFILELINK(src, BASE_D):
    sql = "SELECT * FROM FILE"
    data = await dbSELECT(sql, (), BASE_D)
    for item in data:
        if src in item:
            return True
    return False


async def emailCheckRegularExpression(content):
    # Email-check regular expression
    result = None
    try:
        parts = content.split()
        for part in parts:
            USER_EMAIL = re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", part)
            if len(USER_EMAIL) != 0:
                result = USER_EMAIL[0]
                break
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


async def phoneCheck(content):
    result = None
    try:
        parts = content.split()
        for phone in parts:
            if phone and (str(phone).startswith('+') or str(phone).startswith('8') or str(phone).startswith('9') or str(
                    phone).startswith('7')) and len(str(phone)) >= 10:
                result = phone
                break
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
    finally:
        return result


def isYesNo(msg):
    result = False
    try:
        if msg and str(msg).lower().strip() in ['y', 'yes', 'да', 'д', 'lf', 'l', '1']:
            result = True
    finally:
        return result


def wConf(key, val, CONF_P, INI_D):
    try:
        CONF_P.read(INI_D)
        CONF_P.set(SECTION, key, str(val))

        with open(INI_D, 'w') as configfile:
            CONF_P.write(configfile)
    except Exception as e:
        print(e, 95)


def rConf(key, CONF_P):
    result = None
    try:
        s = CONF_P.get(SECTION, key)
        result = ast.literal_eval(s)
        if len(result) == 0:
            result = None
    finally:
        return result


def getDocIdFromLink(link):
    try:
        begin = link[0:link.rindex('/')].rindex('/') + 1
        end = link.rindex('/')
        link = link[begin:end]
    finally:
        return link


def getTelegramChannel(lan):
    result = 'ferey_channel_english'
    try:
        # chinese
        if lan in ['zh', 'zh-chs', 'zh-cht', 'ja', 'ko', 'zh-CN', 'zh-TW', 'th', 'vi', 'tw', 'sg']:
            result = 'ferey_channel_chinese'
        # arabic    # ir, af
        elif lan in ['ar-XA', 'ar', 'tr', 'ur', 'fa', 'tj', 'dz', 'eg', 'iq', 'sy', 'ae', 'sa', 'tn', 'ir', 'af']:
            result = 'ferey_channel_arabic'
        # spanish   # portugal: 'pt', 'br', 'ao', 'mz'
        elif lan in ['es', 'ar', 'cl', 'co', 'cu', 've', 'bo', 'pe', 'ec', 'pt', 'br', 'ao', 'mz']:
            result = 'ferey_channel_spanish'
        # french
        elif lan in ['fr', 'ch', 'be', 'ca']:
            result = 'ferey_channel_french'
        # europe
        elif lan in ['ru', 'kz', 'kg', 'uz', 'tm', 'md', 'am', 'uk-UA', 'uk', 'kk', 'tk', 'ky']:
            result = 'ferey_channel_europe'
    except Exception as e:
        logger.info(f'\033[{95}m%s\033[0m' % str(e))
    finally:
        return result


def getTelegramGroup(lan):
    result = 'ferey_group_english'
    try:
        # chinese
        if lan in ['zh', 'zh-chs', 'zh-cht', 'ja', 'ko', 'zh-CN', 'zh-TW', 'th', 'vi', 'tw', 'sg']:
            result = 'ferey_group_chinese'
        # arabic    # ir, af
        elif lan in ['ar-XA', 'ar', 'tr', 'ur', 'fa', 'tj', 'dz', 'eg', 'iq', 'sy', 'ae', 'sa', 'tn', 'ir', 'af']:
            result = 'ferey_group_arabic'
        # spanish   # portugal: 'pt', 'br', 'ao', 'mz'
        elif lan in ['es', 'ar', 'cl', 'co', 'cu', 've', 'bo', 'pe', 'ec', 'pt', 'br', 'ao', 'mz']:
            result = 'ferey_group_spanish'
        # french
        elif lan in ['fr', 'ch', 'be', 'ca']:
            result = 'ferey_group_french'
        # europe
        elif lan in ['ru', 'kz', 'kg', 'uz', 'tm', 'md', 'am', 'uk-UA', 'uk', 'kk', 'tk', 'ky']:
            result = 'ferey_group_europe'
    except Exception as e:
        logger.info(f'\033[{95}m%s\033[0m' % str(e))
    finally:
        return result


async def isBad(bot, chat_id, username, CONF_P, EXTRA_D, BASE_D, BASE_S, fields_1):
    result = False
    try:
        if username and (username.startswith('kwpr') or username.startswith('kvpr')):
            result = True
            return

        sql = "SELECT BAD_TID, BAD_OFFERBOT FROM BAD WHERE BAD_TID=?"
        data = await dbSELECT(sql, (chat_id,), BASE_S)
        if not len(data): return
        # BAD_TID, BAD_OFFERBOT = data[0]
        # if not BAD_OFFERBOT:
        if True:
            result = True
            sql = "SELECT USER_TID, USER_USERNAME, USER_FIRSTNAME FROM USER WHERE USER_TID=?"
            data = await dbSELECT(sql, (chat_id,), BASE_D)
            if not len(data): return
            USER_TID, USER_USERNAME, USER_FIRSTNAME = data[0]

            # удалаяем последнюю строку в Google-таблице
            sql = "SELECT USER_TID FROM USER"
            daat = await dbSELECT(sql, (), BASE_D)
            daat = [item[0] for item in daat]
            d1 = [('', '', '', '', '', '', '', '', '', '', '', '')]
            d2 = 'A' + str(len(daat) + 1)
            d12 = (rConf('db_file_id', CONF_P))[0]
            await apiSyncUpdate(d1, d12, d2, CONF_P, EXTRA_D)
            sql = "DELETE FROM USER WHERE USER_TID=?"
            await dbCHANGE(sql, (chat_id,), BASE_D)

            sql = f"SELECT {fields_1} FROM USER"
            value_many = await dbSELECT(sql, (), BASE_D)
            spreadsheetId = (rConf('db_file_id', CONF_P))[0]
            await apiSyncAll(value_many, spreadsheetId, CONF_P, EXTRA_D)
            await sendMyText(bot, my_tid, f"✅ Delete from user @{USER_USERNAME} ({USER_TID}) {USER_FIRSTNAME} ok")
    except Exception as e:
        logger.info(f'\033[{95}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def sendToAdmins(bot, CONF_P, txt):
    try:
        for admin_id in rConf('admin_id', CONF_P):
            try:
                await sendMyText(bot=bot, chat_id=int(admin_id), text=txt)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                await asyncio.sleep(round(random.uniform(1, 2), 2))
        logger.info(f'\033[{92}m%s\033[0m' % txt)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))


async def templateSender(CONF_P, EXTRA_D, MEDIA_D):
    post_media_id = None
    post_media_options = None

    # 1
    post_txt = f'''
🍃 Через 1 час в 20:00 я проведу прямой эфир!

Подключайся и смотри все самые интересные моменты!

🍂 Не пропусти возможность!
Переходи по моей ссылке, встроенной в кнопку.
'''
    post_btn = '🎥 Прямой эфир в instagram'
    post_url = 'https://www.instagram.com'
    post_media_type = 'photo'
    post_media_name = os.path.join(MEDIA_D, (rConf('logo_name', CONF_P))[0])
    post_pin = False
    tmp_date = datetime.datetime.now() + datetime.timedelta(days=3)
    post_time = datetime.datetime(tmp_date.year, tmp_date.month, tmp_date.day, hour=20, minute=0)
    await savePostToGoogleDrive(CONF_P, EXTRA_D, post_txt, post_btn, post_url, post_media_name,
                                post_media_id, post_media_type, post_pin,
                                post_time, post_media_options)

    # 2
    post_txt = f'''
🔥 Как тебе прямой эфир? 
Расскажи об этом. 
Ниже я прикреплю Google-форму обратной связи

При заполнении, пришлю тебе Чек-лист по твоему запросу
'''
    post_btn = '⚠️ Google-форма обратной связи'
    post_url = 'https://docs.google.com/forms/d/e/1FAIpQLSehCkXuL9nCgRvPEdddgTnC99SMW-d_qTPzDjBzbASTAnX_lg/viewform'
    post_media_type = 'photo'
    post_media_name = os.path.join(MEDIA_D, (rConf('logo_name', CONF_P))[0])
    post_pin = True
    tmp_date = datetime.datetime.now() + datetime.timedelta(days=4)
    post_time = datetime.datetime(tmp_date.year, tmp_date.month, tmp_date.day, hour=20, minute=0)
    await savePostToGoogleDrive(CONF_P, EXTRA_D, post_txt, post_btn, post_url, post_media_name,
                                post_media_id, post_media_type, post_pin,
                                post_time, post_media_options)

    # 3
    post_txt = post_btn = post_url = post_pin = None
    post_media_name = os.path.join(MEDIA_D, (rConf('logo_name', CONF_P))[0])
    post_media_type = 'video_note'
    tmp_date = datetime.datetime.now() + datetime.timedelta(days=5)
    post_time = datetime.datetime(tmp_date.year, tmp_date.month, tmp_date.day, hour=20, minute=0)
    await savePostToGoogleDrive(CONF_P, EXTRA_D, post_txt, post_btn, post_url, post_media_name,
                                post_media_id, post_media_type, post_pin,
                                post_time, post_media_options)


async def apiUpdateSendFolder(CONF_P, EXTRA_D, INI_D):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0]), rConf('scopes', CONF_P))
    httpAuth = credentials.authorize(httplib2.Http())
    drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)
    dynamic_folder_name = (rConf('dynamic_folder_id', CONF_P))[0]
    file_list_dic = await apiGetFileList(drive_service, dynamic_folder_name, {})

    tmp = {}
    for k, v in file_list_dic.items():
        try:
            if v[1] == 'application/vnd.google-apps.folder':
                # google_folder.append(v[0])
                tmp[k] = v[0]
                # google_key.append(v[2])
        except Exception as e:
            logger.info(f'\033[{92}m%s\033[0m' % e, 95)
            await asyncio.sleep(round(random.uniform(1, 2), 2))

    tmp = dict(sorted(tmp.items(), key=lambda para: para[-1], reverse=False))
    google_folder = []
    google_key = []
    for k, v in tmp.items():
        google_key.append(k)
        google_folder.append(v)

    # google_folder.sort()
    wConf('google_folder', google_folder, CONF_P, INI_D)
    wConf('google_key', google_key, CONF_P, INI_D)
    logger.info(f'\033[{92}m%s\033[0m' % google_folder)


async def scheduled_hour(part_of_hour, CONF_P, EXTRA_D, INI_D):
    logger.info(f'\033[{92}m%s\033[0m' % 'scheduled_hour ok')
    # await templateSender()
    await apiUpdateSendFolder(CONF_P, EXTRA_D, INI_D)
    await asyncio.sleep(part_of_hour + 200)
    while True:
        logger.info(f'\033[{92}m%s\033[0m' % f'start sending...{str(datetime.datetime.now())}')
        await apiUpdateSendFolder(CONF_P, EXTRA_D, INI_D)
        await asyncio.sleep(one_hour - (datetime.datetime.now()).minute * 60 + 200)


async def scheduled_minute(part_of_minute, bot, CONF_P, EXTRA_D, MEDIA_D, BASE_D):
    logger.info(f'\033[{92}m%s\033[0m' % 'scheduled_minute ok')
    await apiCheckSendFolder(bot, CONF_P, EXTRA_D, MEDIA_D, BASE_D)
    await asyncio.sleep(part_of_minute)
    while True:
        # logger.info(f'\033[{92}m%s\033[0m' % f'start sending...{str(datetime.datetime.now())}')
        await apiCheckSendFolder(bot, CONF_P, EXTRA_D, MEDIA_D, BASE_D)
        await asyncio.sleep(one_minute - datetime.datetime.utcnow().second)


async def readLikes(BASE_D, POST_ID=1):
    cnt = '⁰'
    try:
        sql = "SELECT USER_ID FROM LIKE WHERE POST_ID = ?"
        data = await dbSELECT(sql, (POST_ID,), BASE_D)
        cnt = str(100 + len(data))
        cnt = cnt.replace('0', '⁰').replace('1', '¹').replace('2', '²').replace('3', '³').replace('4', '⁴').replace('5',
                                                                                                                    '⁵').replace(
            '6', '⁶').replace('7', '⁷').replace('8', '⁸').replace('9', '⁹')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return cnt


async def dbHAS_LIKE(USER_ID, POST_ID, BASE_D):
    data = True
    try:
        sql = "SELECT LIKE_ID FROM LIKE WHERE USER_ID=? AND POST_ID=?"
        data = await dbSELECT(sql, (USER_ID, POST_ID,), BASE_D)
        data = True if data else False
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return data


async def randomText(text):
    result = text
    try:
        space_arr = []
        start_pos = 0
        for item in text:
            try:
                if item == ' ':
                    start_pos = (text.find(' ', start_pos)) + 1
                    space_arr.append(start_pos)
            except Exception:
                pass
        if len(space_arr) != 0:
            random_pos = random.choice(space_arr)
            result = f"{text[:random_pos]} {text[random_pos:]}"

        dic_char = {'В': 'B', 'М': '𐌑', 'С': 'Ϲ', 'а': 'a', 'в': 'ʙ', 'р': 'ρ', 'с': 'ϲ', 'п': 'n', 'ш': 'ɯ', 'э': '϶',
                    'к': 'κ'}  # 'и': 'ᥙ',
        arr = ['В', 'М', 'С', 'а', 'в', 'р', 'с', 'п', 'ш', 'э', 'к']  # 'и',
        random_chr = random.choice(arr)
        random_pos = arr.index(random_chr)
        for ix in range(0, random_pos):
            try:
                result = result.replace(arr[ix], dic_char[arr[ix]])
                result = f"{result}​"
            except:
                pass
        result = result[0:1023]
        # result = result.replace('р', 'р')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


def isTID(item):
    result = False
    try:
        result = int(item)
    except Exception:
        # await log(e, 95)
        pass
    finally:
        return result


async def createReplyMarkupButton(bot, group_id, chat_id, offer_id, OFFER_BUTTON, BASE_D):
    result = None
    try:
        if OFFER_BUTTON is None or OFFER_BUTTON == '': return
        tmp = []
        dic_btns = await checkButton(bot, None, OFFER_BUTTON)
        result = types.InlineKeyboardMarkup()
        buttons = []
        for k, v in dic_btns.items():
            try:
                if v[0]:
                    sql = "SELECT * FROM OFFER WHERE OFFER_CHATTID=?"
                    data = await dbSELECT(sql, (group_id,), BASE_D)
                    items = [item[0] for item in data]
                    view_post_id = items.index(offer_id) + 1 if offer_id else len(data)

                    if len(tmp) > 0 and tmp[-1] is None:
                        result.add(*buttons)
                        if str(v[1]).startswith('btn_'):
                            buttons = [types.InlineKeyboardButton(text=str(v[0]), callback_data=f"{v[1]}_{chat_id}_{view_post_id}")]
                        else:
                            buttons = [types.InlineKeyboardButton(text=str(v[0]), url=v[1])]
                    else:
                        if str(v[1]).startswith('btn_'):
                            buttons.append(types.InlineKeyboardButton(text=str(v[0]), callback_data=f"{v[1]}_{chat_id}_{view_post_id}"))
                        else:
                            buttons.append(types.InlineKeyboardButton(text=str(v[0]), url=v[1]))
                tmp.append(v[0])
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                await asyncio.sleep(round(random.uniform(1, 2), 2))
        if len(buttons) > 0:
            result.add(*buttons)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def checkButton(bot, chat_id, txt):
    result = {}
    txt = txt.strip()
    try:
        start_ = []
        finish_ = []
        for ix in range(0, len(txt)):
            try:
                if txt[ix] == '[':
                    start_.append([ix, '['])
                elif txt[ix] == ']':
                    finish_.append([ix, ']'])
                elif txt[ix] == '\n':
                    start_.append([ix, '\n'])
                    finish_.append([ix, '\n'])
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                await asyncio.sleep(round(random.uniform(1, 2), 2))

        if len(start_) != len(finish_): return

        for ix in range(0, len(start_)):
            try:
                if start_[ix][-1] == '\n':
                    result[ix] = [None, None]
                else:
                    tmp = txt[start_[ix][0] + 1: finish_[ix][0]]
                    split_btn = tmp.strip().split('|')
                    if len(split_btn) > 1:
                        btn_name = split_btn[0].strip() if len(split_btn) > 1 else "🔗 Go"
                        btn_link = split_btn[-1].strip()
                        if not await isUrl(btn_link):
                            await sendMyText(bot, chat_id, f"🔗 {btn_link}: invalid")
                            return
                    else:
                        btn_name = split_btn[0]
                        btn_link = cleanhtml(split_btn[0])[:20]
                        btn_link = f"btn_{btn_link.encode('utf-8').hex()}"

                    result[ix] = [btn_name, btn_link]
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                await asyncio.sleep(round(random.uniform(1, 2), 2))
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f"RetryAfter {e.timeout}", 95)
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % e, 95)
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>')
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


async def initBot(dp, bot, ref, message, CONF_P, EXTRA_D, MEDIA_D, BASE_D, fields_1):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "⚙️ Restart"),
        types.BotCommand("lang", "🇫🇷 Language"),
        types.BotCommand("happy", "🐈 Happy"),
    ])
    os.makedirs(MEDIA_D, exist_ok=True, mode=0o777)

    # add and sync USER to db
    if not message.from_user.is_bot:
        sql = "INSERT OR IGNORE INTO USER (USER_TID, USER_DATE,USER_USERNAME, USER_FIRSTNAME, USER_LASTNAME) " \
              "VALUES (?,CURRENT_TIMESTAMP, ?, ?, ?);"
        await dbCHANGE(sql, (message.from_user.id, message.from_user.username, message.from_user.first_name,
        message.from_user.last_name,), BASE_D)
    if ref != '' and ref != str(message.from_user.id):
        sql = "UPDATE USER SET USER_UTM = ? WHERE USER_TID = ?"
        await dbCHANGE(sql, (ref, message.from_user.id,), BASE_D)
    sql = f"SELECT {fields_1} FROM USER"
    value_many = await dbSELECT(sql, (), BASE_D)
    spreadsheetId = (rConf('db_file_id', CONF_P))[0]
    await apiSyncAll(value_many, spreadsheetId, CONF_P, EXTRA_D)

    # pre-upload
    sql = "SELECT * FROM FILE"
    data = await dbSELECT(sql, (), BASE_D)
    if not data:
        scopes = rConf('scopes', CONF_P)
        credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
        httpAuth = credentials.authorize(httplib2.Http())
        drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)
        file_list_dic = await apiGetFileList(drive_service, (rConf('static_folder_id', CONF_P))[0], {})

        for k, v in file_list_dic.items():
            try:
                result = None
                fl_post = await getFromMedia(CONF_P, EXTRA_D, MEDIA_D, BASE_D, v[0], reWrite=True)
                post = types.InputFile(fl_post) if fl_post and '/' in fl_post else fl_post
                mimetype_folder = 'application/vnd.google-apps.folder'
                if await isVideo(fl_post) and v[1] != mimetype_folder and not str(v[0]).endswith('_note.mp4'):
                    result = await bot.send_video(chat_id=my_tid, video=post, caption="")
                elif await isImage(fl_post) and v[1] != mimetype_folder:
                    result = await bot.send_photo(chat_id=my_tid, photo=post, caption="")
                elif str(v[0]).endswith('.ogg') and v[1] != mimetype_folder:
                    result = await bot.send_voice(chat_id=my_tid, voice=post, caption="")
                elif str(v[0]).endswith('.mp3') and v[1] != mimetype_folder:
                    result = await bot.send_audio(chat_id=my_tid, audio=post, caption="")
                elif str(v[0]).endswith('_note.mp4') and v[1] != mimetype_folder:
                    result = await bot.send_video_note(chat_id=my_tid, video_note=post)
                if result:
                    await safeFileId(result, v[0], BASE_D)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % e, 95)
                await asyncio.sleep(round(random.uniform(1, 2), 2))
                print(e)
        logger.info(f'\033[{92}m%s\033[0m' % "pre upload end")


def getPosOfDict(dicti_, pos=1):
    tmp = 1
    for k, v in dicti_.items():
        if tmp == pos:
            return k, v
        tmp += 1
    return None, None


async def getProxy(identifier, EXTRA_D, CONF_P, server=None):
    result = None
    try:
        if rConf('proxy', CONF_P) == 0: return

        with open(os.path.join(EXTRA_D, "proxy.txt"), "r") as f:
            lines = f.readlines()
        random.shuffle(lines)

        for line in lines:
            try:
                hostname, port, username, password = line.strip().split('..')
                # logger.info(f'\033[{92}m%s\033[0m' % f"proxy ({identifier}): {hostname}")
                result = {
                    "scheme": "socks5",
                    "hostname": hostname,
                    "port": int(port),
                    "username": username,
                    "password": password
                }
                break
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % str(e))
                await asyncio.sleep(round(random.uniform(1, 2), 2))
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % f"{str(e)}, {identifier}, {server}")
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def correctLink(link):
    result = link
    try:
        if link.strip() == '':
            result = None
            return
        link = link.strip()
        res = link.split()
        try:
            float(res[0])
            link = str(link.split()[1]).strip('/@\'!')
        except Exception:
            link = str(link.split()[0]).strip('/@\'!')

        if link.startswith('t.me/') and not ('+' in link or 'joinchat' in link):
            link = link.strip('t.me/').strip()
        elif link.startswith('t.me/') and ('+' in link or 'joinchat' in link):
            link = f"https://{link}"
        elif link.endswith('.t.me'):
            link = link.strip('.t.me').strip()
        else:
            if 'http://' in link:
                link = link.replace('http://', 'https://')
            link = link[len(const_url):len(link)] if const_url in link and not (
                    't.me/+' in link or 't.me/joinchat/' in link) else link

        if 'https://telesco.pe/' in link:
            link = link.replace('https://telesco.pe/', '')

        try:
            link = str(int(link))
        except Exception:
            link = link if 't.me/+' in str(link) or 't.me/joinchat/' in str(link) else f"@{link}"

        try:
            if link.split('/')[-1].isdigit():
                link = f"{link[:link.rindex('/')]}"
        except Exception:
            pass

        try:
            if '+' in link:
                link = str(int(link.split('+')[-1]))
        except Exception:
            pass

        try:
            if link.startswith('joinchat/'):
                link = f"t.me/{link}"
            elif link.startswith('@joinchat/'):
                link = link.replace('@', 't.me/')
        except Exception:
            pass

        link = link.lstrip(':-.')
        result = link
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


def isNames(phrase):
    # (?s)\bhello\b.*?\b
    keywords = ['names', 'сотка', 'скорость', 'like', 'концентрат', 'aяз', 'чит-код', "сборная", 'ск-', 'капитан',
                'лагерь']
    for keyword in keywords:
        if keyword.lower() in phrase.lower():
            return True
    return False
# endregion


# region pyrogram
async def getSession(identifier, SESSIONS_D, CONF_P, db=None, isProxy=True):
    res = proxy = None
    try:
        await asyncio.sleep(round(random.uniform(0, 0.1), 2))
        identifier = str(identifier)
        if isTID(identifier):
            sql = "SELECT SESSION_NAME, SESSION_APIID, SESSION_APIHASH,SESSION_PHONE FROM SESSION WHERE SESSION_TID = ?"
            data = await dbSELECT(sql, (identifier,), db)
        else:
            sql = "SELECT SESSION_NAME, SESSION_APIID, SESSION_APIHASH,SESSION_PHONE FROM SESSION WHERE name = ?"
            data = await dbSELECT(sql, (identifier,), db)
        if not data: return

        if isProxy:
            proxy = await getProxy(identifier, CONF_P)

        lock = asyncio.Lock()
        async with lock:
            res = Client(name=os.path.join(SESSIONS_D, data[0][0]), api_id=data[0][1], api_hash=data[0][2],
                         phone_number=data[0][3], proxy=proxy)
        # logger.info(f'\033[{92}m%s\033[0m' % f"getSession end")
    finally:
        return res


async def isChat(bot, chat_id, link, SESSIONS_D, CONF_P, BASE_S, BASE_E, is_history=False):
    result = None
    get_chat_history_count = 0
    try:
        sql = "SELECT SESSION_TID,SESSION_STATUS FROM SESSION WHERE SESSION_SPAM IS NOT '*' LIMIT 10"
        data = await dbSELECT(sql, (), BASE_S)
        random.shuffle(data)
        for item in data:
            SESSION_TID, SESSION_STATUS = item
            if not (await checkSessionFlood(SESSION_TID, BASE_S) and (
                    SESSION_STATUS == '' or SESSION_STATUS is None)): continue
            try:
                link = await correctLink(link)
                if not link: return

                # process
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (f'isChat', SESSION_TID,), BASE_S)

                async with await getSession(SESSION_TID, SESSIONS_D, CONF_P, BASE_S, False) as app:
                    r = await joinChat(bot, app, chat_id, link, SESSION_TID, BASE_S, BASE_E)
                    if r is None: logger.info(f'\033[{92}m%s\033[0m' % f"{link} is None"); return
                    txt_ = f"▪️ Администратор закрытой группы не принял заявки на вступление (напишите @{ferey_telegram_username})"
                    if r == -1:
                        await sendMyText(bot, chat_id, txt_)
                        return
                    result = await app.get_chat(r.id)
                    if is_history:
                        try:
                            get_chat_history_count = await app.get_chat_history_count(r.id)
                        except Exception as e:
                            logger.info(f'\033[{92}m%s\033[0m' % str(e))
                            await asyncio.sleep(round(random.uniform(0, 1), 2))

                    await leaveChat(app, result, link)
                break
            except (FloodWait, SlowmodeWait) as e:
                logger.info(
                    f'\033[{92}m%s\033[0m' % f"Wait: {datetime.datetime.utcfromtimestamp(e.value + 1).strftime('%H:%M:%S')}")
                await asyncio.sleep(round(random.uniform(5, 10), 2))

                till_time = (datetime.datetime.now() + datetime.timedelta(seconds=e.value + 1)).strftime(
                    "%d-%m-%Y_%H-%M")
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                SESSION_STATUS = f'Wait {till_time}'
                await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
            except (UserDeactivatedBan, UserDeactivated, AuthKeyInvalid, AuthKeyUnregistered, AuthKeyDuplicated,
                    SessionExpired,
                    SessionRevoked) as e:
                logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID} deactivated: {str(e)}")
                await asyncio.sleep(round(random.uniform(5, 10), 2))
                await deleteAccountFun(bot, SESSION_TID, SESSIONS_D, CONF_P, BASE_S)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID}: {str(e)}")
                await asyncio.sleep(round(random.uniform(1, 2), 2))
            finally:
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result, get_chat_history_count


async def isInviteChat(bot, chat_id, link, SESSIONS_D, CONF_P, BASE_S, BASE_E):
    result = None
    try:
        sql = "SELECT SESSION_TID,SESSION_STATUS FROM SESSION WHERE SESSION_SPAM IS NOT '*'"
        data = await dbSELECT(sql, (), BASE_S)
        random.shuffle(data)
        for item in data:
            SESSION_TID, SESSION_STATUS = item
            if not (await checkSessionFlood(SESSION_TID, BASE_S) and (
                    SESSION_STATUS == '' or SESSION_STATUS is None)): continue
            try:
                link = await correctLink(link)
                if not link: continue

                # process
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (f'isChat', SESSION_TID,), BASE_S)

                async with await getSession(SESSION_TID, SESSIONS_D, CONF_P, BASE_S) as app:
                    r = await joinChat(bot, app, chat_id, link, SESSION_TID, BASE_S, BASE_E)

                    # get_chat https://t.me/+KO7_fV4aGKZkYTUy
                    if r == -1 or r is None: return
                    r = await app.get_chat(r.id)
                    logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID} get_chat {r.id}")

                    if not (r.type.value in ['group', 'supergroup']):
                        text = "🚶 Вставь ссылку на группу, а не канал"
                        await sendMyText(bot, chat_id, text)
                    elif hasattr(r.permissions, 'can_invite_users') and not r.permissions.can_invite_users:
                        text = "🚶 Зайди в «Разрешения» группы и включи <i>участникам группы</i> возможность: «Добавление участников»"
                        await sendMyText(bot, chat_id, text)
                    else:
                        text = "🚶 Начинаем проверку группы..\n#длительность 2мин"
                        await sendMyText(bot, chat_id, text)
                        # await asyncio.sleep(rConf('AWAIT_JOIN'))

                        try:
                            get_chat_member = await app.get_chat_member(chat_id=r.id, user_id=int(SESSION_TID))
                            result = True if get_chat_member and get_chat_member.status.value == 'member' else False
                        except Exception as e:
                            logger.info(f'\033[{92}m%s\033[0m' % str(e))
                            await asyncio.sleep(round(random.uniform(1, 2), 2))

                    # leave_chat
                    await leaveChat(app, r, link)
                break
            except (FloodWait, SlowmodeWait) as e:
                logger.info(
                    f'\033[{92}m%s\033[0m' % f"Wait: {datetime.datetime.utcfromtimestamp(e.value + 1).strftime('%H:%M:%S')}")
                await asyncio.sleep(round(random.uniform(5, 10), 2))

                till_time = (datetime.datetime.now() + datetime.timedelta(seconds=e.value + 1)).strftime(
                    "%d-%m-%Y_%H-%M")
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                SESSION_STATUS = f'Wait {till_time}'
                await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
            except (UserDeactivatedBan, UserDeactivated, AuthKeyInvalid, AuthKeyUnregistered, AuthKeyDuplicated,
                    SessionExpired,
                    SessionRevoked) as e:
                logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID} deactivated: {str(e)}")
                await asyncio.sleep(round(random.uniform(5, 10), 2))
                await deleteAccountFun(bot, SESSION_TID, SESSIONS_D, CONF_P, BASE_S)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID}: {str(e)}")
                await asyncio.sleep(round(random.uniform(1, 2), 2))
            finally:
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def joinChat(bot, app, chat_id, link, SESSION_TID, BASE_S, BASE_E):
    result = None
    try:
        if 't.me/c/' in str(link):
            try:
                tmp = link.strip('https://t.me/c/').split('/')[0]
                peer_channel = await app.resolve_peer(int(f"-100{tmp}"))
                result = await app.invoke(functions.channels.JoinChannel(channel=peer_channel))
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % str(e))
        else:
            result = await app.join_chat(link)
        await asyncio.sleep(1)
    except (FloodWait, SlowmodeWait) as e:
        text = f'\033[{92}m%s\033[0m' % f"Wait: {datetime.datetime.utcfromtimestamp(e.value + 1).strftime('%H:%M:%S')}"
        logger.info(text)
        await asyncio.sleep(round(random.uniform(5, 10), 2))

        till_time = (datetime.datetime.now() + datetime.timedelta(seconds=e.value + 1)).strftime("%d-%m-%Y_%H-%M")
        sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
        SESSION_STATUS = f'Wait {till_time}'
        await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
    except UserAlreadyParticipant as e:
        logger.info(f'\033[{92}m%s\033[0m' % f"UserAlreadyParticipant {link}: {str(e)}")
        try:
            result = await app.get_chat(link)
        except Exception:
            pass
    except (InviteHashExpired, InviteHashInvalid) as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        try:
            result = await app.join_chat(link)
        except Exception:
            await sendMyText(bot, chat_id, f"▪️ Ссылка на чат {link} не валидна (или попробуйте еще раз)")
    except (UsernameInvalid, UsernameNotOccupied, ChannelBanned) as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
        await sendMyText(bot, chat_id, f"▪️ Ссылка/username на группу {link} не валидна")
        await deleteInvalidChat(link, BASE_E)
    except BadRequest as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(2, 3), 2))

        try:
            result = await app.join_chat(link)
        except Exception:
            result = -1
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def leaveChat(app, r, link):
    try:
        chat_id = r.id if r and ('t.me/+' in str(link) or 'joinchat/' in str(link)) else link
        like_names_res = isNames(r.title)
        if not (like_names_res or (r.username and f'ferey' in r.username)):
            await app.leave_chat(chat_id, True)
            await asyncio.sleep(round(random.uniform(1, 2), 2))
            # logger.info(f'\033[{92}m%s\033[0m' % f"\t{link} leave chat")
    except (FloodWait, SlowmodeWait) as e:
        logger.info(
            f'\033[{92}m%s\033[0m' % f"Wait: {datetime.datetime.utcfromtimestamp(e.value + 1).strftime('%H:%M:%S')}")
        await asyncio.sleep(e.value + 1)
    except Exception:
        # logger.info(f'\033[{92}m%s\033[0m' % f"leaveChat_error: {link} {str(e)}")
        await asyncio.sleep(round(random.uniform(5, 10), 2))


async def getChatMembers(bot, chat_id, link, SESSIONS_D, CONF_P, BASE_S, BASE_E):
    result = []
    try:
        text = f"🚶 Проверяем участников группы..\n#длительность 1мин"
        await sendMyText(bot, chat_id, text)
        sql = "SELECT SESSION_TID,SESSION_STATUS FROM SESSION WHERE SESSION_SPAM IS NOT '*'"
        data = await dbSELECT(sql, (), BASE_S)
        random.shuffle(data)
        for item in data:
            tmp_members = []
            SESSION_TID, SESSION_STATUS = item
            if not (await checkSessionFlood(SESSION_TID, BASE_S) and (
                    SESSION_STATUS == '' or SESSION_STATUS is None)): continue
            try:
                link = await correctLink(link)
                if not link: continue

                # process
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (f'getChatMembers', SESSION_TID,), BASE_S)

                async with await getSession(SESSION_TID, SESSIONS_D, CONF_P, BASE_S) as app:
                    r = await joinChat(bot, app, chat_id, link, SESSION_TID, BASE_S, BASE_E)

                    # get members
                    sql = "SELECT SESSION_TID FROM SESSION"
                    data_ = await dbSELECT(sql, (), BASE_S)
                    data_ = [str(item[0]) for item in data_]
                    try:
                        async for member in app.get_chat_members(r.id, filter=enums.ChatMembersFilter.SEARCH):
                            if member.user.username and not member.user.is_bot and not member.user.is_deleted and not member.user.is_scam and not member.user.is_fake and not member.user.is_support and str(
                                    member.user.id) not in data_:
                                tmp_members.append(member.user.username)
                    except ChatAdminRequired as e:
                        logger.info(f'\033[{92}m%s\033[0m' % str(e))
                        await sendMyText(bot, chat_id, f"🔺 Требуются права админа")
                        return
                    except Exception as e:
                        logger.info(f'\033[{92}m%s\033[0m' % str(e))

                    # leave chat
                    await leaveChat(app, r, link)

                    result = tmp_members
                    break
            except (FloodWait, SlowmodeWait) as e:
                logger.info(
                    f'\033[{92}m%s\033[0m' % f"Wait: {datetime.datetime.utcfromtimestamp(e.value + 1).strftime('%H:%M:%S')}")
                await asyncio.sleep(round(random.uniform(5, 10), 2))

                till_time = (datetime.datetime.now() + datetime.timedelta(seconds=e.value + 1)).strftime(
                    "%d-%m-%Y_%H-%M")
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                SESSION_STATUS = f'Wait {till_time}'
                await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
            except (UserDeactivatedBan, UserDeactivated, AuthKeyInvalid, AuthKeyUnregistered, AuthKeyDuplicated,
                    SessionExpired,
                    SessionRevoked) as e:
                logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID} deactivated: {str(e)}")
                await asyncio.sleep(round(random.uniform(5, 10), 2))
                await deleteAccountFun(bot, SESSION_TID, SESSIONS_D, CONF_P, BASE_S)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % f"{SESSION_TID}: {str(e)}")
                await asyncio.sleep(round(random.uniform(1, 2), 2))
            finally:
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (SESSION_STATUS, SESSION_TID,), BASE_S)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def savePhoto(bot, photo, MEDIA_D):
    result = None
    try:
        if not photo: return
        file_id = photo.big_file_id
        photo_path = os.path.join(MEDIA_D, (datetime.datetime.utcnow()).strftime("%d-%m-%Y_%H-%M-%S.jpg"))
        await bot.download_file_by_id(file_id, photo_path)

        # jpg, .jpeg, .png, .gif and .mp4
        if os.path.exists(photo_path) and os.path.getsize(photo_path) < 5242880:
            try:
                telegraph = Telegraph()
                res = telegraph.upload_file(photo_path)
                if res:
                    result = f"{'https://telegra.ph'}{res[0]['src']}"
                    if os.path.exists(photo_path): os.remove(photo_path)
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % str(e))
                await asyncio.sleep(round(random.uniform(1, 2), 2))
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % f"{str(e)}")
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def deleteAccountFun(bot, SESSION_TID, SESSIONS_D, CONF_P, BASE_S):
    try:
        sql = "SELECT SESSION_NAME FROM SESSION WHERE SESSION_TID=?"
        data = await dbSELECT(sql, (SESSION_TID,), BASE_S)
        if not data:
            await sendToAdmins(bot, CONF_P, f"✅ Account {SESSION_TID} doesnt exist")
            return
        data = await dbSELECT(sql, (SESSION_TID,), BASE_S)
        if not len(data): return
        SESSION_NAME = data[0][0]
        SESSION_NAME = os.path.join(SESSIONS_D, f'{SESSION_NAME}.session')

        sql = "DELETE FROM SESSION WHERE SESSION_TID = ?"
        await dbCHANGE(sql, (SESSION_TID,), BASE_S)

        sql = "DELETE FROM COMPANY WHERE COMPANY_FROMUSERTID = ?"
        await dbCHANGE(sql, (SESSION_TID,), BASE_S)

        if os.path.exists(SESSION_NAME):
            os.remove(SESSION_NAME)
        await sendToAdmins(bot, CONF_P, f"✅ deleteAccount {SESSION_TID} ok")
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f"RetryAfter {e.timeout}")
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))


async def deleteInvalidChat(chat, BASE_E):
    sql = "DELETE FROM CHANNEL WHERE CHANNEL_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    sql = "DELETE FROM CHAT WHERE CHAT_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    sql = "DELETE FROM USER WHERE USER_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    sql = "DELETE FROM BOT WHERE BOT_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    chat = chat.strip('@')

    sql = "DELETE FROM CHANNEL WHERE CHANNEL_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    sql = "DELETE FROM CHAT WHERE CHAT_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    sql = "DELETE FROM USER WHERE USER_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    sql = "DELETE FROM BOT WHERE BOT_USERNAME=?"
    await dbCHANGE(sql, (chat,), BASE_E)

    chat = chat if 'https://' in chat else f"@{chat}"
    # await sendToAdmins(f"deleteInvalidChat {chat}")


async def checkSessionFlood(SESSION_TID, BASE_S):
    result = SESSION_TID
    try:
        sql = "SELECT SESSION_STATUS FROM SESSION WHERE SESSION_TID = ?"
        data = await dbSELECT(sql, (SESSION_TID,), BASE_S)
        if not data: return

        t_t = str(data[0][0]).split()
        if len(t_t) == 2:
            date_ = t_t[1].split('_')[0]
            time_ = t_t[1].split('_')[1]

            day = int(date_.split('-')[0])
            month = int(date_.split('-')[1])
            year = int(date_.split('-')[2])
            hour = int(time_.split('-')[0])
            minute = int(time_.split('-')[1])

            diff = datetime.datetime.now() - datetime.datetime(year=year, month=month, day=day, hour=hour,
                                                               minute=minute)

            if diff.days >= 0:
                sql = "UPDATE SESSION SET SESSION_STATUS = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (None, SESSION_TID,), BASE_S)
                result = SESSION_TID
            else:
                result = None
    except Exception:
        # logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def checkSessionLimit(SESSION_TID, LIMIT_NAME, LIMIT, BASE_S):
    result = SESSION_TID
    try:
        sql = f"SELECT {LIMIT_NAME} FROM SESSION WHERE SESSION_TID = ?"
        data = await dbSELECT(sql, (SESSION_TID,), BASE_S)
        if not data: return

        t_t = str(data[0][0]).split()
        if len(t_t) == 2:
            msg_by_day = int(t_t[0])
            date_ = t_t[1].split('-')

            day = int(date_[0])
            month = int(date_[1])
            year = int(date_[2])

            diff = datetime.datetime.now() - datetime.datetime(year=year, month=month, day=day)

            if diff.days > 0:
                result = f"0 {datetime.datetime.now().strftime('%d-%m-%Y')}"
                sql = f"UPDATE SESSION SET {LIMIT_NAME} = ? WHERE SESSION_TID = ?"
                await dbCHANGE(sql, (result, SESSION_TID,), BASE_S)
            elif msg_by_day < LIMIT:
                result = SESSION_TID
            else:
                result = None
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result


async def INVITEDAY_CHECK(CONF_P, BASE_S, threshold=0):
    result = 0
    try:
        sql = "SELECT SESSION_TID,SESSION_INVITEDAY FROM SESSION WHERE SESSION_SPAM IS NOT '*'"
        data = await dbSELECT(sql, (), BASE_S)
        for item in data:
            try:
                SESSION_TID, SESSION_INVITEDAY = item
                INVITEDAY_LIMIT_ = rConf('INVITEDAY_LIMIT', CONF_P)
                checkSessionLimit_ = await checkSessionLimit(SESSION_TID, 'SESSION_INVITEDAY', INVITEDAY_LIMIT_, BASE_S)
                if SESSION_INVITEDAY == '' or SESSION_INVITEDAY is None:
                    result += INVITEDAY_LIMIT_
                elif await checkSessionFlood(SESSION_TID, BASE_S) and checkSessionLimit_:
                    result += rConf('INVITEDAY_LIMIT', CONF_P) - int(SESSION_INVITEDAY.split()[0])
            except Exception as e:
                logger.info(f'\033[{92}m%s\033[0m' % str(e))
                await asyncio.sleep(round(random.uniform(1, 2), 2))

        result = int(result * 0.6)
        if threshold:
            result = result if result < threshold else threshold
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return result
# endregion


# region apiGoogle
async def apiSyncAll(value_many, spreadsheetId, CONF_P, EXTRA_D, range_many='A2', sheetId='Sheet1',
                     valueInputOption='USER_ENTERED',
                     majorDimension="ROWS"):
    scopes = rConf('scopes', CONF_P)
    credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
    httpAuth = credentials.authorize(httplib2.Http())
    sheets_service = build('sheets', 'v4', http=httpAuth, cache_discovery=False)

    convert_value = []
    for item in value_many:
        convert_value.append(list(item))

    await apiWriteCells(sheets_service, convert_value, range_many, spreadsheetId, sheetId, valueInputOption,
                        majorDimension)


async def apiSyncUpdate(value_many, spreadsheetId, range_many, CONF_P, EXTRA_D, sheetId='Sheet1',
                        valueInputOption='USER_ENTERED',
                        majorDimension="ROWS"):
    try:
        if range_many is None:
            logger.info(f'\033[{92}m%s\033[0m' % 'range_many is None')
            return
        scopes = rConf('scopes', CONF_P)
        credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
        httpAuth = credentials.authorize(httplib2.Http())
        sheets_service = build('sheets', 'v4', http=httpAuth, cache_discovery=False)

        convert_value = []
        for item in value_many:
            convert_value.append(list(item))

        await apiWriteCells(sheets_service, convert_value, range_many, spreadsheetId, sheetId, valueInputOption,
                            majorDimension)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))


async def apiFindRowByTID(USER_TID, CONF_P, EXTRA_D, sheetId='Sheet1'):
    result = None
    try:
        scopes = rConf('scopes', CONF_P)
        credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
        httpAuth = credentials.authorize(httplib2.Http())
        sheets_service = build('sheets', 'v4', http=httpAuth, cache_discovery=False)
        spreadsheetId = (rConf('db_file_id', CONF_P))[0]

        values_list = sheets_service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=sheetId,
                                                                 fields='values').execute().get('values', [])

        row = 0
        for ix, item in enumerate(values_list):
            if str(USER_TID) in item:
                row = ix + 1
                break
        result = 'A' + str(row)
    finally:
        return result


async def apiWriteCells(sheets_service, value_many, range_many, spreadsheetId, sheetId, valueInputOption,
                        majorDimension="ROWS"):
    result = False
    try:
        result = sheets_service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
            "valueInputOption": valueInputOption,
            "data": [{
                "range": f"{sheetId}!{range_many}",
                "majorDimension": majorDimension,
                "values": value_many,
            }]}).execute()
        logger.info(f'\033[{92}m%s\033[0m' % 'write to db ok')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
    finally:
        return result


async def apiAppendCells(sheets_service, value_many, spreadsheetId, valueInputOption):
    result = True
    try:
        sheets_service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range='A1',
                                                      valueInputOption=valueInputOption,
                                                      body={"values": value_many}).execute()

        logger.info(f'\033[{92}m%s\033[0m' % 'write to db ok')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        result = False
    return result


async def apiReadCells(sheets_service, range_many, spreadsheetId, sheetId='Sheet1'):
    result = None
    try:
        r = sheets_service.spreadsheets().values().batchGet(
            spreadsheetId=spreadsheetId, ranges=f"{sheetId}!{range_many}"
        ).execute()

        result = r.get('valueRanges', [])[0]['values'] if len(r.get('valueRanges', [])) > 0 else None
        logger.info(f'\033[{92}m%s\033[0m' % 'read from db ok')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
    finally:
        return result


def get_random_color():
    """
    Создаю случайный цвет с альфа каном
    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#Color
    :return:
    """
    return {
        "red": randrange(0, 255) / 255,
        "green": randrange(0, 255) / 255,
        "blue": randrange(0, 255) / 255,
        "alpha": randrange(0, 10) / 10  # 0.0 - прозрачный
    }


def apiCreateFileOrFolder(drive_service, mimeType, name, parent_id):
    creation_id = None
    try:
        body = {
            'name': name,
            'mimeType': mimeType,
            'parents': [parent_id],
            'properties': {'title': 'titleSpreadSheet', 'locale': 'ru_RU'},
            'locale': 'ru_RU'
        }
        result_folder = drive_service.files().create(body=body, fields='id').execute()
        creation_id = result_folder['id']
    finally:
        return creation_id


async def sendCopy(bot, cnt, USER_TID, USER_USERNAME, result):
    try:
        # USER_TID = 5150111687
        await bot.copy_message(chat_id=int(USER_TID), from_chat_id=result.chat.id, message_id=result.message_id,
                               reply_markup=result.reply_markup)
        cnt += 1
        logger.info(f'\033[{92}m%s\033[0m' % f"\t{cnt}. send to user {USER_TID}-{USER_USERNAME} ok")
        await asyncio.sleep(0.05)
    except RetryAfter as e:
        logger.info(f'\033[{92}m%s\033[0m' % f"RetryAfter {e.timeout}")
        await asyncio.sleep(e.timeout)
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
        logger.info(f'\033[{92}m%s\033[0m' % f"\tsend to user {USER_TID}-{USER_USERNAME} error")
        await asyncio.sleep(round(random.uniform(1, 2), 2))
    finally:
        return cnt


async def apiCheckSendFolder(bot, CONF_P, EXTRA_D, MEDIA_D, BASE_D):
    google_folder = rConf('google_folder', CONF_P)
    google_key = rConf('google_key', CONF_P)
    cnt = 0

    for folder in google_folder:
        try:
            USER_TID = USER_USERNAME = None
            sql = "SELECT USER_TID, USER_USERNAME FROM USER"
            data = await dbSELECT(sql, (), BASE_D)
            result = None
            fix_utc_now = datetime.datetime.utcnow()

            for user in data:
                try:
                    USER_TID, USER_USERNAME = user
                    user_datetime = fix_utc_now + datetime.timedelta(hours=0)
                    user_datetime = datetime.datetime(year=user_datetime.year, month=user_datetime.month,
                                                      day=user_datetime.day, hour=user_datetime.hour,
                                                      minute=user_datetime.minute)
                    # log(f"{user_datetime} and {datetime.datetime.strptime(folder, '%d-%m-%Y %H:%M')}")

                    # if True:
                    #     g_post_time_utc = '01-04-2022 09:00'
                    if user_datetime == datetime.datetime.strptime(folder, "%d-%m-%Y %H:%M"):
                        logger.info(f'\033[{92}m%s\033[0m' % f"\t! CHECK {folder}")
                        logger.info(f'\033[{92}m%s\033[0m' % f"\tprepare send to {USER_TID} {USER_USERNAME}")
                        if result:
                            cnt = await sendCopy(bot, cnt, USER_TID, USER_USERNAME, result)
                            continue

                        # drive service
                        credentials = ServiceAccountCredentials.from_json_keyfile_name(
                            os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0]),
                            rConf('scopes', CONF_P))
                        httpAuth = credentials.authorize(httplib2.Http())
                        drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)

                        # скачали
                        k_info = post_media = ''
                        dynamic_folder_name = google_key[google_folder.index(folder)]
                        # dynamic_folder_name = (rConf('dynamic_folder_id'))[0]
                        file_list_dic = await apiGetFileList(drive_service, dynamic_folder_name, {})
                        for k, v in file_list_dic.items():
                            try:
                                if v[0] == 'info':  # and v[2] == f"{g_post_time_utc}+{delta_hour}":
                                    k_info = k
                                # and v[2] == f"{g_post_time_utc}+{delta_hour}":
                                elif v[1] != 'application/vnd.google-apps.folder':
                                    post_media = await apiDlFile(drive_service, k, v[0], v[1], MEDIA_D)
                                    logger.info(f'\033[{92}m%s\033[0m' % f'\tdl {v[0]} ok')
                            except Exception as e:
                                logger.info(f'\033[{92}m%s\033[0m' % str(e))
                                await asyncio.sleep(round(random.uniform(1, 2), 2))

                        # sheets service
                        credentials = ServiceAccountCredentials.from_json_keyfile_name(
                            os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0]),
                            rConf('scopes', CONF_P))
                        httpAuth = credentials.authorize(httplib2.Http())
                        sheets_service = build('sheets', 'v4', http=httpAuth, cache_discovery=False)

                        # get meta from info
                        values_list_values = sheets_service.spreadsheets().values()
                        values_get = values_list_values.get(spreadsheetId=k_info, range='Sheet1', fields='values')
                        values_list = values_get.execute().get('values', [])
                        logger.info(f'\033[{92}m%s\033[0m' % f'\tdl info ok')
                        post_txt = values_list[0][1] if len(values_list[0]) > 1 else ''
                        post_btn = (values_list[1][1]) if len(values_list[1]) > 1 and values_list[1][1] else None
                        post_url = (values_list[2][1]) if len(values_list[2]) > 1 and values_list[2][1] else None
                        post_media_type = values_list[4][1] if len(values_list[4]) > 1 and values_list[4][1] else None
                        post_pin = isYesNo(values_list[5][1]) if len(values_list[5]) > 1 else False

                        url = post_url if post_url else None
                        text = post_btn if post_btn else "🔗 GO"
                        inline_add = types.InlineKeyboardButton(text=text, url=url)
                        reply_markup = types.InlineKeyboardMarkup().add(inline_add) if post_url else None
                        # по умолчанию мы перезаписываем reWrite=True, но в этом случае когда мы работаем с рассылкой,
                        # то мы удаляем файл чуть выше, и загружаем

                        logger.info(f'\033[{92}m%s\033[0m' % '\tbefore send')
                        if post_media_type and post_media_type == 'photo':
                            result = await sendMyPhoto(
                                bot=bot,
                                chat_id=int(USER_TID),
                                photo_name=post_media,
                                caption=post_txt,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'animation':  # gif == mp4
                            result = await sendMyAnimation(
                                bot=bot,
                                chat_id=int(USER_TID),
                                animation_name=post_media,
                                caption=post_txt,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'video':
                            result = await sendMyVideo(
                                bot=bot,
                                chat_id=int(USER_TID),
                                video_name=post_media,
                                caption=post_txt,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'audio':  # m4a, mp3, ogg + Listen Title
                            result = await sendMyAudio(
                                bot=bot,
                                chat_id=int(USER_TID),
                                audio_name=post_media,
                                caption=post_txt,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'voice':  # m4a, mp3, ogg
                            result = await sendMyVoice(
                                bot=bot,
                                chat_id=int(USER_TID),
                                voice_name=post_media,
                                caption=post_txt,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'video_note':  # < 1 min
                            result = await sendMyVideoNote(
                                bot=bot,
                                chat_id=int(USER_TID),
                                videonote_name=post_media,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'document':
                            result = await sendMyDoc(
                                bot=bot,
                                chat_id=int(USER_TID),
                                doc_name=post_media,
                                caption=post_txt,
                                CONF_P=CONF_P,
                                EXTRA_D=EXTRA_D,
                                MEDIA_D=MEDIA_D,
                                BASE_D=BASE_D,
                                reply_markup=reply_markup,
                                reWrite=False
                            )
                        elif post_media_type and post_media_type == 'poll':
                            result = await sendMyPoll(
                                bot=bot,
                                chat_id=int(USER_TID),
                                question=post_txt,
                                options=post_media,
                                reply_markup=reply_markup
                            )
                        elif post_txt != '':
                            result = await sendMyText(
                                bot=bot,
                                chat_id=int(USER_TID),
                                text=post_txt,
                                reply_markup=reply_markup)
                        elif post_txt == '' and post_url:
                            result = await bot.send_message(
                                chat_id=int(USER_TID),
                                text=f"<a href='{post_url}'>🔗 Переходи по ссылке</a>",
                                reply_markup=reply_markup
                            )
                        # проверить чему равно result если первый из USER_TID заблокирует бота

                        if post_pin:
                            await bot.pin_chat_message(chat_id=USER_TID, message_id=result.message_id,
                                                       disable_notification=False)
                        cnt += 1
                        logger.info(f'\033[{92}m%s\033[0m' % f"\t{cnt}. send to user {USER_TID}-{USER_USERNAME} ok")
                except RetryAfter as e:
                    logger.info(f'\033[{92}m%s\033[0m' % f"RetryAfter {e.timeout}")
                    await asyncio.sleep(e.timeout)
                except Exception as e:
                    logger.info(f'\033[{92}m%s\033[0m' % str(e))
                    logger.info(f'\033[{92}m%s\033[0m' % f"\tsend to user {USER_TID}-{USER_USERNAME} error")
                    await asyncio.sleep(round(random.uniform(1, 2), 2))
        except Exception as e:
            logger.info(f'\033[{92}m%s\033[0m' % str(e))
            await asyncio.sleep(round(random.uniform(1, 2), 2))
    if cnt:
        logger.info(f'\033[{92}m%s\033[0m' % f"-----send to users cnt = {cnt}-----")


async def apiGetFileList(drive_service, folder_id, tmp_dic={} or None, parent_name='', isFile=False):
    if isFile:
        file = drive_service.files().get(fileId=folder_id, fields="id, name, size, modifiedTime, mimeType").execute()
        tmp_dic[file['id']] = [file['name'], file['mimeType'], parent_name, file['modifiedTime']]
        return tmp_dic
    q = "\'" + folder_id + "\'" + " in parents"
    fields = "nextPageToken, files(id, name, size, modifiedTime, mimeType)"
    results = drive_service.files().list(pageSize=1000, q=q, fields=fields).execute()
    items = results.get('files', [])
    for item in items:
        try:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                tmp_dic[item['id']] = [item['name'], item['mimeType'], parent_name, item['modifiedTime']]
                await apiGetFileList(drive_service, item['id'], tmp_dic, item['name'])
            else:
                tmp_dic[item['id']] = [item['name'], item['mimeType'], parent_name, item['modifiedTime']]
        except Exception as e:
            logger.info(f'\033[{92}m%s\033[0m' % str(e))

    tmp_dic_2 = {}
    for k, v in reversed(tmp_dic.items()):
        tmp_dic_2[k] = v

    return tmp_dic_2


async def uploadFile(drive_service, name, post_media_name, folder_id):
    result = None
    try:
        if name == 'нет' or name is None: return

        request_ = drive_service.files().create(
            media_body=MediaFileUpload(filename=post_media_name, resumable=True),
            body={'name': name, 'parents': [folder_id]}
        )
        response = None
        while response is None:
            status, response = request_.next_chunk()
            if status: logger.info(f'\033[{92}m%s\033[0m' % "Uploaded %d%%." % int(status.progress() * 100))
        logger.info(f'\033[{92}m%s\033[0m' % "Upload Complete!")
        # if os.path.exists(post_media_name):
        #     os.remove(post_media_name)
        result = True
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
    finally:
        return result


async def apiDlFile(drive_service, id_, name, gdrive_mimeType, MEDIA_D):
    save_mimeType = None
    file_name = add = ''

    if gdrive_mimeType.endswith('document') and not (name.endswith('doc') or name.endswith('docx')):
        save_mimeType = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    elif gdrive_mimeType.endswith('sheet') and not (name.endswith('xls') or name.endswith('xlsx')):
        save_mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif gdrive_mimeType.endswith('presentation') and not (name.endswith('ppt') or name.endswith('pptx')):
        save_mimeType = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    elif gdrive_mimeType == 'application/vnd.google-apps.folder':
        return ''

    if save_mimeType:
        request_ = drive_service.files().export_media(fileId=id_, mimeType=save_mimeType)
    else:
        request_ = drive_service.files().get_media(fileId=id_)

    if request_:
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request_)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            logger.info(f'\033[{92}m%s\033[0m' % "Download %d%%." % int(status.progress() * 100))

        if gdrive_mimeType.endswith('.spreadsheet'):
            add = '.xlsx'
        elif gdrive_mimeType.endswith('.document'):
            add = '.docx'
        elif gdrive_mimeType.endswith('.presentation'):
            add = '.pptx'
        file_name = returnCuttedFileName(name, add, MEDIA_D)
        with io.open(file_name, 'wb') as f:
            fh.seek(0)
            f.write(fh.read())
        await asyncio.sleep(1)
    return file_name


def returnCuttedFileName(name, add, MEDIA_D):
    file_name = f'{MEDIA_D}/{name}{add}'
    l_ = len(file_name)
    diff = 255 - l_
    if diff <= 0:
        ext = getExt(name)
        name = name[0:len(name) - 1 - abs(diff) - len(ext)] + ext
        file_name = f'{MEDIA_D}/{name}{add}'
    return file_name


def getNameWithoutExt(file_name):
    name = file_name
    try:
        ext = getExt(name)
        if ext != '':
            index_ext = str(name).rindex(ext)
            index_slash = str(name).rindex('/') + 1 if '/' in name else 0
            name = name[index_slash:index_ext]
    finally:
        return name


def getExt(name):
    ext = ''
    try:
        index = str(name).rindex('.')
        ext = name[index:len(name)]
        if len(ext) > 5:
            ext = ''
    finally:
        return ext


async def isNeedForCreate(file_list_dic, unit, mimeType, name, CONF_P, INI_D):
    flag = False
    for k, v in file_list_dic.items():
        if v[0] == name and v[1] == mimeType:
            flag = True
            wConf(getNewKeyConfig(name, CONF_P, INI_D), [k], CONF_P, INI_D)
            break
    if not flag: unit.append(name)
    return unit


def isExistGoogleId(file_list_dic, mimeType, name, parentName):
    result = None
    for k, v in file_list_dic.items():
        if v[0] == name and v[1] == mimeType and v[2] == parentName:
            return k
    return result


def getNewKeyConfig(value, CONF_P, INI_D):
    new_key = ''
    try:
        CONF_P.read(INI_D)
        for k, v in CONF_P.items('CONFIG'):
            if value == ast.literal_eval(v)[0]:
                arr = str(k).split('_')
                new_key = f'{arr[0]}_{arr[1]}_id'
                break
    finally:
        return new_key


async def apiInit(CONF_P, INI_D, EXTRA_D, fields_0):
    scopes = rConf('scopes', CONF_P)
    credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
    httpAuth = credentials.authorize(httplib2.Http())
    drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)
    file_list_dic = await apiGetFileList(drive_service, (rConf('share_folder_id', CONF_P))[0], {})

    subfolders = []
    mimeType_folder = 'application/vnd.google-apps.folder'
    static_folder_name = (rConf('static_folder_name', CONF_P))[0]
    dynamic_folder_name = (rConf('dynamic_folder_name', CONF_P))[0]
    subfolders = await isNeedForCreate(file_list_dic, subfolders, mimeType_folder, static_folder_name, CONF_P, INI_D)
    subfolders = await isNeedForCreate(file_list_dic, subfolders, mimeType_folder, dynamic_folder_name, CONF_P, INI_D)
    for i in range(0, len(subfolders)):
        share_folder_id = (rConf('share_folder_id', CONF_P))[0]
        creation_id = apiCreateFileOrFolder(drive_service, mimeType_folder, subfolders[i], share_folder_id)
        wConf(getNewKeyConfig(subfolders[i], CONF_P, INI_D), [creation_id], CONF_P, INI_D)

    files = []
    mimeType_sheet = 'application/vnd.google-apps.spreadsheet'
    db_file_name = (rConf('db_file_name', CONF_P))[0]
    files = await isNeedForCreate(file_list_dic, files, mimeType_sheet, db_file_name, CONF_P, INI_D)
    for i in range(0, len(files)):
        db_file_name = (rConf('db_file_name', CONF_P))[0]
        mimeType_sheet = 'application/vnd.google-apps.spreadsheet'
        share_folder_id = (rConf('share_folder_id', CONF_P))[0]
        creation_id = apiCreateFileOrFolder(drive_service, mimeType_sheet, db_file_name, share_folder_id)
        wConf(getNewKeyConfig(files[i], CONF_P, INI_D), [creation_id], CONF_P, INI_D)
        value_many = [fields_0]
        spreadsheetId = (rConf('db_file_id', CONF_P))[0]
        await apiSyncAll(value_many, spreadsheetId, CONF_P, EXTRA_D, 'A1')
    logger.info(f'\033[{92}m%s\033[0m' % 'api init ok')


async def getCellDialog(range_many, CONF_P, EXTRA_D):
    scopes = rConf('scopes', CONF_P)
    credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
    httpAuth = credentials.authorize(httplib2.Http())
    sheets_service = build('sheets', 'v4', http=httpAuth, cache_discovery=False)
    spreadsheetId = '1sQWH3NpJAh8t4QDmP-8vvc7XaCTx4Uflc6LADA9zvN8'
    sheetId = 'Лист1'

    result = None
    try:
        ranges = f"{sheetId}!{range_many}"
        r = sheets_service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId, ranges=ranges).execute()
        if ':' in range_many:
            result = r.get('valueRanges', [])[0]['values'] if len(r.get('valueRanges', [])) > 0 else None
            result = [item[0] for item in result]
        else:
            result = r.get('valueRanges', [])[0]['values'][0][0] if len(r.get('valueRanges', [])) > 0 else None
        logger.info(f'\033[{92}m%s\033[0m' % 'read from db ok')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))
    finally:
        return result


async def getListOfSendFolder(CONF_P, EXTRA_D):
    scopes = rConf('scopes', CONF_P)
    credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
    httpAuth = credentials.authorize(httplib2.Http())
    drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)

    tmp = []
    file_list_dic = await apiGetFileList(drive_service, (rConf('dynamic_folder_id', CONF_P))[0], {})
    for k, v in file_list_dic.items():
        try:
            parentFolder = v[2]
            nameFolder = v[0]
            datetime_ = datetime.datetime.now()
            if parentFolder == '' and datetime_ < datetime.datetime.strptime(nameFolder, "%d-%m-%Y %H:%M"):
                tmp.append([nameFolder, k])
        except Exception as e:
            logger.info(f'\033[{92}m%s\033[0m' % str(e))

    return tmp


async def savePostToGoogleDrive(CONF_P, EXTRA_D, post_txt, post_btn, post_url, post_media_name,
                                post_media_id, post_media_type, post_pin,
                                post_time, post_media_options, post_users='*'):
    try:
        scopes = rConf('scopes', CONF_P)
        credential_file = os.path.join(EXTRA_D, (rConf('credential_file', CONF_P))[0])
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scopes)
        httpAuth = credentials.authorize(httplib2.Http())
        drive_service = build('drive', 'v3', http=httpAuth, cache_discovery=False)
        file_list_dic = await apiGetFileList(drive_service, (rConf('dynamic_folder_id', CONF_P))[0], {})

        mimeType_folder = 'application/vnd.google-apps.folder'
        id_TimeFolder = isExistGoogleId(file_list_dic, mimeType_folder, post_time.strftime("%d-%m-%Y %H:%M"), '')
        if id_TimeFolder is None:
            id_TimeFolder = apiCreateFileOrFolder(drive_service, 'application/vnd.google-apps.folder',
                                                  post_time.strftime("%d-%m-%Y %H:%M"),
                                                  (rConf('dynamic_folder_id', CONF_P))[0])

        mimeType_sheet = 'application/vnd.google-apps.spreadsheet'
        id_InfoXlsx = isExistGoogleId(file_list_dic, mimeType_sheet, 'info', post_time.strftime("%d-%m-%Y %H:%M"))
        if id_InfoXlsx is None:
            mimeType_sheet = 'application/vnd.google-apps.spreadsheet'
            id_InfoXlsx = apiCreateFileOrFolder(drive_service, mimeType_sheet, 'info', id_TimeFolder)
            v_m = [["текст", "кнопка(имя)", "кнопка(ссылка)", "медиа", "медиа тип", "закрепить(pin)", "пользователи"]]
            spreadsheetId = id_InfoXlsx
            await apiSyncAll(
                value_many=v_m,
                spreadsheetId=spreadsheetId,
                CONF_P=CONF_P,
                EXTRA_D=EXTRA_D,
                range_many='A1',
                majorDimension="COLUMNS"
            )

        name = os.path.basename(post_media_name) if post_media_name else 'нет'
        if post_media_type == 'poll':
            post_txt = post_media_name
            name = str(post_media_options)
        else:
            await uploadFile(drive_service, name, post_media_name, id_TimeFolder)

        v_m = [[post_txt, post_btn if post_btn else 'no', post_url if post_url else 'no', name,
                post_media_type if post_media_type else 'no',
                'yes' if post_pin else 'no', post_users]]
        spreadsheetId = id_InfoXlsx
        await apiSyncAll(
            value_many=v_m,
            spreadsheetId=spreadsheetId,
            CONF_P=CONF_P,
            EXTRA_D=EXTRA_D,
            range_many='B1',
            majorDimension="COLUMNS"
        )
        logger.info(f'\033[{92}m%s\033[0m' % 'save to google ok')
    except Exception as e:
        logger.info(f'\033[{92}m%s\033[0m' % str(e))

# endregion


# region notes
# sys.path.append('../hub')
# print("In module products sys.path[0], __package__ ==", sys.path[-1], __package__)
# from .. .hub import xtra
# dp.register_chosen_inline_handler(chosen_inline_handler_fun, lambda chosen_inline_result: True)
# dp.register_inline_handler(inline_handler_main, lambda inline_handler_main_: True)
# channel_post_handler
# edited_channel_post_handler
# poll_handler - а это получается реакция на размещение опроса
# poll_answer_handler - реакция на голосование
# chat_join_request_handler
# errors_handler
# current_state

# apt install redis -y
# nano /etc/redis/redis.conf
# systemctl restart redis.service
# systemctl status redis
# redis-cli
# netstat -lnp | grep redis


# endregion
