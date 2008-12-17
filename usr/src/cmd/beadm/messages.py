#!/usr/bin/python
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#
# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.
#
# beadm - The Boot Environment Administration tool.
#
# A module containing all of the messages output by beadm.

import sys

class Msgs:

	# Indices corresponding to message numbers for beadm.
	(BEADM_ERR_ACTIVATE,
	BEADM_ERR_BE_EXISTS,
	BEADM_ERR_SNAP_EXISTS,
	BEADM_ERR_CREATE,
	BEADM_ERR_DESTROY,
	BEADM_ERR_DESTROY_ACTIVE,
	BEADM_ERR_BE_DOES_NOT_EXIST,
	BEADM_ERR_NO_BES_EXIST,
	BEADM_ERR_MSG_SUB,
	BEADM_ERR_ILL_SUBCOMMAND,
	BEADM_ERR_INVALID_RESPONSE,
	BEADM_ERR_LIST,
	BEADM_ERR_LIST_DATA,
	BEADM_ERR_LOG_CREATE,
	BEADM_ERR_LOG_RM,
	BEADM_ERR_MOUNT,
	BEADM_ERR_MOUNT_EXISTS,
	BEADM_ERR_MOUNTED,
	BEADM_ERR_MOUNTPOINT,
	BEADM_ERR_MUTUALLY_EXCL,
	BEADM_ERR_NO_MSG,
	BEADM_ERR_NO_ZPOOL,
	BEADM_ERR_NOT_SUPPORTED_NGZ,
	BEADM_ERR_OPT_ARGS,
	BEADM_ERR_OS,
	BEADM_ERR_PERMISSIONS,
	BEADM_ERR_RENAME,
	BEADM_ERR_SHARED_FS,
	BEADM_ERR_SNAP_DOES_NOT_EXISTS,
	BEADM_ERR_UNMOUNT,
	BEADM_ERR_UNMOUNT_ACTIVE,
	BEADM_ERR_BENAME,
	BEADM_MSG_ACTIVE_ON_BOOT,
	BEADM_MSG_DESTROY,
	BEADM_MSG_DESTROY_NO,
	BEADM_MSG_BE_CREATE_START,
	BEADM_MSG_BE_CREATE_SUCCESS,
	BEADM_MSG_FREE_FORMAT,
	) = range(38)

	# Indices corresponding to message numbers for libbe that we are
	# interested in expanding messages.
	(BE_ERR_ACCESS,
	BE_ERR_ACTIVATE_CURR,
	BE_ERR_AUTONAME,
	BE_ERR_BE_NOENT,
	BE_ERR_BUSY,
	BE_ERR_CANCELED,
	BE_ERR_CLONE,
	BE_ERR_COPY,
	BE_ERR_CREATDS,
	BE_ERR_CURR_BE_NOT_FOUND,
	BE_ERR_DESTROY,
	BE_ERR_DEMOTE,
	BE_ERR_DSTYPE,
	BE_ERR_BE_EXISTS,
	BE_ERR_INIT,
	BE_ERR_INTR,
	BE_ERR_INVAL,
	BE_ERR_INVALPROP,
	BE_ERR_INVALMOUNTPOINT,
	BE_ERR_MOUNT,
	BE_ERR_MOUNTED,
	BE_ERR_NAMETOOLONG,
	BE_ERR_NOENT,
	BE_ERR_POOL_NOENT,
	BE_ERR_NODEV,
	BE_ERR_NOTMOUNTED,
	BE_ERR_NOMEM,
	BE_ERR_NONINHERIT,
	BE_ERR_NXIO,
	BE_ERR_NOSPC,
	BE_ERR_NOTSUP,
	BE_ERR_OPEN,
	BE_ERR_PERM,
	BE_ERR_UNAVAIL,
	BE_ERR_PROMOTE,
	BE_ERR_ROFS,
	BE_ERR_READONLYDS,
	BE_ERR_READONLYPROP,
	BE_ERR_SS_EXISTS,
	BE_ERR_SS_NOENT,
	BE_ERR_UMOUNT,
	BE_ERR_UMOUNT_CURR_BE,
	BE_ERR_UMOUNT_SHARED,
	BE_ERR_UNKNOWN,
	BE_ERR_ZFS,
	BE_ERR_DESTROY_CURR_BE,
	BE_ERR_GEN_UUID,
	BE_ERR_PARSE_UUID,
	BE_ERR_NO_UUID,
	BE_ERR_ZONE_NO_PARENTBE,
	BE_ERR_ZONE_MULTIPLE_ACTIVE,
	BE_ERR_ZONE_NO_ACTIVE_ROOT,
	BE_ERR_ZONE_ROOT_NOT_LEGACY,
	BE_ERR_NO_MOUNTED_ZONE,
	BE_ERR_MOUNT_ZONEROOT,	
	BE_ERR_UMOUNT_ZONEROOT,
	BE_ERR_ZONES_UNMOUNT
	) = range(4000, 4057)

	# Error message dictionaries.
	mBeadmErr = {}
	mBeadmOut = {}
	mBeadmLog = {}
	
	# Errors from beadm (to stderr).
	mBeadmErr[BEADM_ERR_ACTIVATE] = "Unable to activate %(0)s.\n%(1)s"
	mBeadmErr[BEADM_ERR_BE_EXISTS] = "BE %s already exists. Please choose a different BE name."
	mBeadmErr[BEADM_ERR_BE_DOES_NOT_EXIST] = "%s does not exist or appear to be a valid BE.\nPlease check that the name of the BE provided is correct."
	mBeadmErr[BEADM_ERR_NO_BES_EXIST] = "No boot environments found on this system."
	mBeadmErr[BEADM_ERR_CREATE] = "Unable to create %(0)s.\n%(1)s"
	mBeadmErr[BEADM_ERR_DESTROY] = "Unable to destroy %(0)s.\n%(1)s"
	mBeadmErr[BEADM_ERR_DESTROY_ACTIVE] = "%(0)s is the currently active BE and cannot be destroyed.\nYou must boot from another BE in order to destroy %(1)s."
	mBeadmErr[BEADM_ERR_MSG_SUB] = "Fatal error. No message associated with index %d"
	mBeadmErr[BEADM_ERR_ILL_SUBCOMMAND] = "Illegal subcommand %s"
	mBeadmErr[BEADM_ERR_INVALID_RESPONSE] = "Invalid response. Please enter 'y' or 'n'."
	mBeadmErr[BEADM_ERR_LIST] = "Unable to display Boot Environment: %s"
	mBeadmErr[BEADM_ERR_LIST_DATA] = "Unable to process list data."
	mBeadmErr[BEADM_ERR_LOG_CREATE] = "Unable to create log file."
	mBeadmErr[BEADM_ERR_LOG_RM] = "Unable to remove %s"
	mBeadmErr[BEADM_ERR_MOUNT] = "Unable to mount %(0)s.\n%(1)s"
	mBeadmErr[BEADM_ERR_MOUNT_EXISTS] = "%s is already mounted.\nPlease unmount the BE before mounting it again."
	mBeadmErr[BEADM_ERR_MOUNTED] = "Unable to destroy %(0)s.\nIt is currently mounted and must be unmounted before it can be destroyed.\nUse 'beadm unmount %(1)s' to unmount the BE before destroying\nit or 'beadm destroy -fF %(2)s'."
	mBeadmErr[BEADM_ERR_MOUNTPOINT] = "Invalid mount point %s. Mount point must start with a /."
	mBeadmErr[BEADM_ERR_MUTUALLY_EXCL] = "Invalid options: %s are mutually exclusive."
	mBeadmErr[BEADM_ERR_NO_MSG] = "Unable to find message for error code: %d"
	mBeadmErr[BEADM_ERR_NO_ZPOOL] = "BE: %s was not found in any pool.\nThe pool may not exist or the name of the BE is not correct."
	mBeadmErr[BEADM_ERR_NOT_SUPPORTED_NGZ] = "beadm is not supported in a non-global zone."
	mBeadmErr[BEADM_ERR_OPT_ARGS] = "Invalid options and arguments:"
	mBeadmErr[BEADM_ERR_OS] = "System error: %s"
	mBeadmErr[BEADM_ERR_RENAME] = "Rename of BE %(0)s failed.\n%(1)s"
	mBeadmErr[BEADM_ERR_SHARED_FS] = "%s is a shared file system and it cannot be unmounted."
	mBeadmErr[BEADM_ERR_SNAP_DOES_NOT_EXISTS] = "%s does not exist or appear to be a valid snapshot.\nPlease check that the name of the snapshot provided is correct."
	mBeadmErr[BEADM_ERR_SNAP_EXISTS] = "Snapshot %s already exists.\nPlease choose a different snapshot name."
	mBeadmErr[BEADM_ERR_UNMOUNT] = "Unable to unmount %(0)s.\n%(1)s"
	mBeadmErr[BEADM_ERR_UNMOUNT_ACTIVE] = "%s is the currently active BE.\nIt cannot be unmounted unless another BE is the currently active BE."
	mBeadmErr[BE_ERR_ZONES_UNMOUNT] = "Unable to destroy one of %(0)s's zone BE's.\nUse 'beadm destroy -fF %(1)s' or 'zfs -f destroy <dataset>'."
	mBeadmErr[BEADM_ERR_PERMISSIONS] = "You have insufficient privileges to execute this command.\nEither use 'pfexec' to execute the command or become superuser."	
	mBeadmErr[BEADM_ERR_BENAME] = "The BE name provided is invalid.\nPlease check it and try again."

	# Catchall
	mBeadmErr[BEADM_MSG_FREE_FORMAT] = "%s"

	# Messages from beadm (to stdout).
	mBeadmOut[BEADM_MSG_ACTIVE_ON_BOOT] = "The BE that was just destroyed was the 'active on boot' BE.\n%s is now the 'active on boot' BE. Use 'beadm activate' to change it.\n"
	mBeadmOut[BEADM_MSG_DESTROY] = "Are you sure you want to destroy %s? This action cannot be undone(y/[n]):"
	mBeadmOut[BEADM_MSG_DESTROY_NO] = "%s has not been destroyed.\n"
	    
	# Messages from beadm (to log only).
	mBeadmLog[BEADM_MSG_BE_CREATE_START] = "Attempting to create %s"
	mBeadmLog[BEADM_MSG_BE_CREATE_SUCCESS] = "%s was created successfully"

msgLog, msgOut, msgErr = range(3)

def printLog(str, logFd):

	sendMsg(str, msgLog, logFd)

def printStdout(str, logFd):

	sendMsg(str, msgOut, logFd)

def printStderr(str, logFd):

	sendMsg(str, msgErr, logFd)

def composeMsg(str, txt=None):

	# Compose the message to be dispayed.
	# txt can be either a list or string object.
	# Return the newly composed string.

	try:
		msg = str % txt
	except TypeError:
		msg = str

	return (msg)

def sendMsg(str, mode, logFd=-1):
        if mode == msgOut: print >> sys.stdout, str,
        if mode == msgErr: print >> sys.stderr, str
        if logFd != -1 or mode == msgLog: logFd.write(str + "\n")

def printMsg(msgIdx=-1, txt="", logFd=-1):

	# Print the message based on the message index
	if Msgs.mBeadmErr.has_key(msgIdx):
		printStderr(composeMsg(Msgs.mBeadmErr[msgIdx], txt),
		    logFd)
	elif Msgs.mBeadmOut.has_key(msgIdx):
		printStdout(composeMsg(Msgs.mBeadmOut[msgIdx], txt),
		    logFd)
	elif Msgs.mBeadmLog.has_key(msgIdx):
		printLog(composeMsg(Msgs.mBeadmLog[msgIdx], txt), logFd)
	else:
		printStderr(composeMsg(Msgs.mLibbe[BEADM_ERR_MSG_SUB],
		    msgIdx), -1)
		sys.exit(1)

def getMsg(msgIdx=-1, txt=""):

	# Print the message based on the message index
	if Msgs.mBeadmErr.has_key(msgIdx):
		return(composeMsg(Msgs.mBeadmErr[msgIdx], txt))
	elif Msgs.mBeadmOut.has_key(msgIdx):
		return(composeMsg(Msgs.mBeadmOut[msgIdx], txt))
	elif Msgs.mBeadmLog.has_key(msgIdx):
		return(composeMsg(Msgs.mBeadmLog[msgIdx], txt))
	else:
		return(composeMsg(Msgs.mLibbe[BEADM_ERR_MSG_SUB]))
		sys.exit(1)
